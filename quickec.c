#include <unistd.h>
#include <stdio.h>
#include <errno.h>
#include <string.h>
#include <stdint.h>
#include <sys/mman.h>
#include <fcntl.h>
#include <stdlib.h>

struct EcRamField {
	const char* name;
	uint8_t byte_offset;
	uint8_t bit_offset;
	uint8_t bit_size;
	bool allow_set;
};

#define ECRAM_OFFSET 0xFE0B0300
#define ECRAM_LEN    0xFF


const struct EcRamField fields[] = {
	{ /*ITSM*/ "preformence_mode", 0x15, 2, 3, true },
	{ /*BKLC*/ "backlight_control", 0x11, 2, 1, true}
	// { "lid_status", 0x10, 0, 1, false },
	{ /*ACIN*/ "plugged_in", 0x80, 0, 1, false},
	{ /*RSOC*/ "charge", 0x92, 0, 8, false},
	{ /*BTCC*/ "bat_cycles", 0x95, 0, 16, false},


};

#define FIELD_COUNT (sizeof(fields) / sizeof(struct EcRamField))

void print_help(){
	char field_str[FIELD_COUNT * 32] = {0};
	char* temp = field_str;

	for (int i = 0; i < FIELD_COUNT; i++){
		const char* src = fields[i].name;
		size_t len = strlen(src);
		
		memcpy(temp, src, len);
		temp += len;

		if (i != FIELD_COUNT-1){
			memcpy(temp, ", ", 2);
			temp += 2;
		}
	}
	*temp = 0;


	fprintf(stderr, 
		"Quick EC - A program for working with known EC fields safely. Written by PsychedelicPalimpsest\n"
		"Usage: quickec [get/set] [field] [number to set]\n"
		"Available fields: %s\n", field_str);
}






int main(int argc, char **argv) {
	const struct EcRamField* current_field = NULL;
	if (argc <= 2){
		print_help();
		return 1;
	}

	// First arg MUST be get or set
	if (strcmp(argv[1], "get") && strcmp(argv[1], "set")){
		print_help();
		return 1;
	}

	for (int i=0; i < FIELD_COUNT; i++){
		if (strcmp(argv[2], fields[i].name)) continue;

		current_field = &fields[i];
		break;
	}
	// Exit if the user didn't specify a correct field
	if (!current_field){
		print_help();
		return 1;
	}

	// Check for root privileges
	if (getuid() != 0 && setuid(0) != 0) {
		fprintf(stderr, "Could not acquire root via setuid. Error: %s\n", strerror(errno));
		return 1;
	}




	int fd = open("/dev/mem", O_RDWR | O_SYNC);
	if (fd < 0) {
		fprintf(stderr, "Failed to open /dev/mem: %s\n", strerror(errno));
		return 1;
	}

	size_t pagesize = getpagesize();
	size_t page_base = ECRAM_OFFSET & ~(pagesize - 1);
	size_t page_offset = ECRAM_OFFSET - page_base;

	void* map = mmap(NULL, pagesize, PROT_READ | PROT_WRITE, MAP_SHARED, fd, page_base);
	if (map == MAP_FAILED) {
		fprintf(stderr, "Cannot map EC RAM into memory space: %s\n", strerror(errno));
		close(fd);
		return 1;
	}

	uint8_t* mem = (uint8_t*)map + page_offset;


	if (0 == strcmp(argv[1], "get")){
		uint64_t val = *(uint64_t*) &mem[current_field->byte_offset];
		val >>= current_field->bit_offset;
		val &= (1ULL << current_field->bit_size) - 1;
		printf("%llu\n", val);
	}else {
		if (!current_field->allow_set){
			fprintf(stderr, "This field does NOT support being set.\n");
			return 1;
		}


		if (!argv[3]) goto INVALID_NUM;

		errno = 0;
		uint64_t setval = (uint64_t) strtol(argv[3], NULL, 0);
		if (errno) goto INVALID_NUM;


		
		uint64_t mask = ( (1ULL << current_field->bit_size) - 1 ) << current_field->bit_offset;
		
		uint64_t set_value = *(uint64_t*) &mem[current_field->byte_offset];

		set_value = (set_value & (~mask)) | ( (setval << current_field->bit_offset) & mask);

		*(uint64_t*) &mem[current_field->byte_offset] = set_value;
		

 		goto CLEANUP;

		INVALID_NUM:
		fprintf(stderr, "Invalid number\n");
		return 1;
	}
	CLEANUP:
	// Cleanup
	munmap(map, pagesize);
	close(fd);

	return 0;
}
