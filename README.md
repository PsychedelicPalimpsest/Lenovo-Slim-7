# Lenovo Slim 7 (16IAH7) EcRam research

This repo is to document my reasearch into my laptop. I will use this info to help figure out ways it interop my linux setup with my laptop.


## My findings

You can switch your power profiles witb the following

| Power profile         | Command                     |
|-----------------------|-----------------------------|
| Power Save            | sudo ectool -w 0x15 -z 0x69 |
| "Intelligent Cooling" | sudo ectool -w 0x15 -z 0x65 |
| "Extreme Performance"  | sudo ectool -w 0x15 -z 0x71 |


Copy from ec ram
```
sudo dd if=/dev/mem bs=1 count=255 skip=$((0xFE0B0300)) iflag=skip_bytes > eram_dump.bin
```



---------------

## Legal

All python code, scripts, and docs are GPL and FDL. Any DSL code is disassembled from my firmware, and is intelectual property of Lenovo.
