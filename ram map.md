## EcRam locations


|Name            |Byte offset     |Inner bit offset|Bit length      |Comment         |
|----------------|----------------|----------------|----------------|----------------|
|ECMV            |0x0             |0               |8               |                |
|ECSV            |0x1             |0               |8               |                |
|ECTV            |0x2             |0               |8               |                |
|ECRV            |0x3             |0               |8               |                |
|S3LB            |0x4             |0               |8               |                |
|S3HB            |0x5             |0               |8               |                |
|S3RS            |0x6             |0               |8               |                |
|TSR1            |0x7             |0               |8               |                |
|TSR2            |0x8             |0               |8               |                |
|TSR3            |0x9             |0               |8               |                |
|TSR4            |0xa             |0               |8               |                |
|TSR5            |0xb             |0               |8               |                |
|TSR6            |0xc             |0               |8               |                |
|TSR7            |0xd             |0               |8               |                |
|TSR8            |0xe             |0               |8               |                |
|BDRV            |0xf             |0               |8               |                |
|LSTE            |0x10            |0               |1               | Lid status? Related: _SB_.PC00.LPCB.H_EC.LSTE |
|LID2            |0x10            |1               |1               |                |
|BKTS            |0x10            |2               |1               |                |
|EKTS            |0x10            |3               |1               |                |
|SMAF            |0x10            |4               |1               |                |
|S4RF            |0x10            |5               |1               |                |
|LDRV            |0x10            |6               |2               |                |
|LDSW            |0x11            |0               |1               |                |
|ISTD            |0x11            |1               |1               |???? IBSM == One IEPM == One : zero, one on "SET auto mode" |
|BKLC            |0x11            |2               |1               |Backlight control. Zero = on, One = off                |
|LESR            |0x11            |3               |1               |???? Set in \_SB_.WMIS. Zero if Arg1 == 0x03, One if Arg1 == 0x02|
|BBAT            |0x11            |4               |1               |                |
|IAPM            |0x11            |5               |1               |???? IBSM == One || IEPM == One : zero |
|IAQM            |0x11            |6               |1               |???? IBSM == One : zero                |
|LIDR            |0x11            |7               |1               |                |
|PCMD            |0x12            |0               |8               |                |
|OKF0            |0x13            |0               |1               |                |
|OKF1            |0x13            |1               |1               |                |
|OKF2            |0x13            |2               |1               |                |
|OKF3            |0x13            |3               |1               |                |
|OKF4            |0x13            |4               |1               |                |
|OKRV            |0x13            |5               |3               |                |
|TXLK            |0x14            |0               |1               |                |
|ECUP            |0x14            |1               |1               |???? Always zero? Related: Name (ECUP, One) |
|FNSP            |0x14            |2               |1               |                |
|NOVB            |0x14            |3               |1               |                |
|CRIS            |0x14            |4               |1               |                |
|CRIL            |0x14            |5               |1               |                |
|SARS            |0x14            |6               |1               |                |
|FNRV            |0x14            |7               |1               |                |
|AOUF            |0x15            |0               |1               | When set, ors the HALS return with 0x80  |
|GFXF            |0x15            |1               |1               |                |
|ITSM            |0x15            |2               |3               | Preformence mod. "Intelligent Cooling": 1, Power save: 2, "Extreme Performance": 4  |
|DKIN            |0x16            |0               |1               |                |
|DKPW            |0x16            |1               |1               |                |
|DKRS            |0x16            |2               |1               |                |
|WFEN            |0x16            |3               |1               |                |
|TPEN            |0x16            |4               |1               |                |
|BLOF            |0x16            |5               |1               |                |
|PB10            |0x16            |6               |1               |                |
|ODRV            |0x16            |7               |1               |                |
|AOUB            |0x17            |0               |1               |                |
|NAOU            |0x17            |1               |1               |                |
|KBBL            |0x17            |2               |1               |                |
|                |0x17            |3               |3               |                |
|HING            |0x17            |6               |1               |                |
|LEMD            |0x17            |7               |1               | If one, and ACIN & 1, does something??     |
|                |0x18            |0               |2               |                |
|DISV            |0x18            |2               |1               |                |
|                |0x18            |3               |1               |                |
|KLED            |0x18            |4               |1               |                |
|                |0x18            |5               |2               |                |
|SLSR            |0x18            |7               |1               |                |
|OSTP            |0x19            |0               |8               |                |
|PJID            |0x1a            |0               |8               |                |
|KBTP            |0x1b            |0               |8               |                |
|SMPT            |0x1c            |0               |8               |                |
|SMST            |0x1d            |0               |8               |                |
|SMAD            |0x1e            |0               |8               |                |
|SMCD            |0x1f            |0               |8               |                |
|SMDA            |0x20            |0               |256             |                |
|SMBT            |0x40            |0               |8               |                |
|SMAA            |0x41            |0               |8               |                |
|SMD1            |0x42            |0               |8               |                |
|SMD2            |0x43            |0               |8               |                |
|BIPT            |0x48            |0               |32              |                |
|BOPT            |0x4c            |0               |32              |                |
|PMSF            |0x70            |0               |1               |                |
|SBMM            |0x72            |0               |8               |                |
|ITSC            |0x7f            |0               |8               |                |
|ACIN            |0x80            |0               |1               | Is plugged in  |
|BTIN            |0x80            |1               |1               | Batery related, controls BAT0._STA return |
|BTST            |0x80            |2               |3               | Batery related, controls PKG1     |
|                |0x80            |5               |1               |                |
|PWRV            |0x80            |6               |2               |                |
|ADPW            |0x81            |0               |8               |                |
|BTSN            |0x82            |0               |16              |                |
|BTDC            |0x84            |0               |16              |                |
|BTDV            |0x86            |0               |16              |                |
|BTFC            |0x88            |0               |16              |                |
|BTTP            |0x8a            |0               |16              | Counts up from 3090               |
|BTCT            |0x8c            |0               |16              |                |
|BTPR            |0x8e            |0               |16              |                |
|BTVT            |0x90            |0               |16              |                |
|RSOC            |0x92            |0               |8               | Relative state of charge as a precent     |
|BSB0            |0x93            |0               |1               | No BSBS have any refs                |
|BSB1            |0x93            |1               |1               |                |
|BSB2            |0x93            |2               |1               |                |
|BSB3            |0x93            |3               |1               |                |
|BSB4            |0x93            |4               |1               |                |
|BSB5            |0x93            |5               |1               |                |
|BSB6            |0x93            |6               |1               |                |
|BSB7            |0x93            |7               |1               |                |
|BSB8            |0x94            |0               |1               |                |
|BSB9            |0x94            |1               |1               |                |
|BSBA            |0x94            |2               |1               |                |
|BSBB            |0x94            |3               |1               |                |
|BSBC            |0x94            |4               |1               |                |
|BSBD            |0x94            |5               |1               |                |
|BSBE            |0x94            |6               |1               |                |
|BSBF            |0x94            |7               |1               |                |
|BTCC            |0x95            |0               |16              |Batery related                |
|ADWT            |0x97            |0               |8               |                |
|MFNM            |0x98            |0               |2               |                |
|DENM            |0x98            |2               |2               |                |
|BTRV            |0x98            |4               |4               |                |
|BTMD            |0x9a            |0               |16              |                |
|BTTM            |0x9c            |0               |16              |                |
|ECEC            |0xa0            |0               |8               |                |
|PAR1            |0xa1            |0               |8               |Maybe related to PARM, by not PAR(number)s are used    |
|PAR2            |0xa2            |0               |8               |                |
|PAR3            |0xa3            |0               |8               |                |
|PAR4            |0xa4            |0               |8               |                |
|PAR5            |0xa5            |0               |8               |                |
|PAR6            |0xa6            |0               |8               |                |
|PAR7            |0xa7            |0               |8               |                |
|PBFU            |0xa8            |0               |1               |MHCF func arg0, when ECAV does bit stuff     |
|A8RV            |0xa8            |1               |7               |Controls first and secound field of MHIF return value, under certain conditions                |
|FULB            |0xa9            |0               |8               |Always 128      |
|FUHB            |0xaa            |0               |8               |Always 0        |
|KBLM            |0xab            |0               |4               |                |
|KBLS            |0xab            |4               |4               |                |
|IDCP            |0xac            |0               |8               |                |
|VCMD            |0xb0            |0               |8               |                |
|VDAT            |0xb1            |0               |8               |                |
|VSTA            |0xb2            |0               |8               |                |
|LSK2            |0xb7            |0               |8               |                |
|BTFW            |0xb8            |0               |64              |                |
|VER1            |0xc0            |0               |8               |                |
|VER2            |0xc1            |0               |8               |                |
|RSV1            |0xc2            |0               |8               |                |
|RSV2            |0xc3            |0               |8               |                |
|CCI0            |0xc4            |0               |8               | USB - OPM read to EC     |
|CCI1            |0xc5            |0               |8               |                |
|CCI2            |0xc6            |0               |8               |                |
|CCI3            |0xc7            |0               |8               |                |
|CTL0            |0xc8            |0               |8               | USB - OPM write to EC   |
|CTL1            |0xc9            |0               |8               |                |
|CTL2            |0xca            |0               |8               |                |
|CTL3            |0xcb            |0               |8               |                |
|CTL4            |0xcc            |0               |8               |                |
|CTL5            |0xcd            |0               |8               |                |
|CTL6            |0xce            |0               |8               |                |
|CTL7            |0xcf            |0               |8               |                |
|MGI0            |0xd0            |0               |8               | USB - OPM read to EC                |
|MGI1            |0xd1            |0               |8               |                |
|MGI2            |0xd2            |0               |8               |                |
|MGI3            |0xd3            |0               |8               |                |
|MGI4            |0xd4            |0               |8               |                |
|MGI5            |0xd5            |0               |8               |                |
|MGI6            |0xd6            |0               |8               |                |
|MGI7            |0xd7            |0               |8               |                |
|MGI8            |0xd8            |0               |8               |                |
|MGI9            |0xd9            |0               |8               |                |
|MGIA            |0xda            |0               |8               |                |
|MGIB            |0xdb            |0               |8               |                |
|MGIC            |0xdc            |0               |8               |                |
|MGID            |0xdd            |0               |8               |                |
|MGIE            |0xde            |0               |8               |                |
|MGIF            |0xdf            |0               |8               |                |
|MGO0            |0xe0            |0               |8               | USB - OPM write to EC                 |
|MGO1            |0xe1            |0               |8               |                |
|MGO2            |0xe2            |0               |8               |                |
|MGO3            |0xe3            |0               |8               |                |
|MGO4            |0xe4            |0               |8               |                |
|MGO5            |0xe5            |0               |8               |                |
|MGO6            |0xe6            |0               |8               |                |
|MGO7            |0xe7            |0               |8               |                |
|MGO8            |0xe8            |0               |8               |                |
|MGO9            |0xe9            |0               |8               |                |
|MGOA            |0xea            |0               |8               |                |
|MGOB            |0xeb            |0               |8               |                |
|MGOC            |0xec            |0               |8               |                |
|MGOD            |0xed            |0               |8               |                |
|MGOE            |0xee            |0               |8               |                |
|MGOF            |0xef            |0               |8               |                |
|USDC            |0xf8            |0               |8               | USB - OPM write to EC                |
|USGC            |0xf9            |0               |8               |                |
|BTPE            |0xfb            |0               |8               |                |



# ChatGPT guessed the following info

Assume the following is wrong unless proven otherwise


## **Power Management / Battery / Charging**

* `ECMV`, `ECSV`, `ECTV`, `ECRV`: Possibly EC measured/expected/current/mode voltages.
* `BDRV`: Battery Drive? Or Battery Drain Voltage?
* `LDRV`: Likely Lid Drive or Battery Level Drive (bitfield).
* `PCMD`: Power Command?
* `OKF0`-`OKF4`: Some kind of status flags or thresholds (OK Flags).
* `ACIN`: AC adapter plugged in.
* `PWRV`: Power state value.
* `ADPW`: Adapter Power rating.
* `BTIN`: Battery insert status.
* `BTST`: Battery status (bitfield).
* `BTSN`: Battery serial number.
* `BTDC`: Battery design capacity.
* `BTDV`: Battery design voltage.
* `BTFC`: Full charge capacity.
* `BTTP`: Battery temperature?
* `BTCT`: Battery current.
* `BTPR`: Battery present rate?
* `BTVT`: Battery voltage.
* `RSOC`: Relative state of charge (%).
* `BTCC`: Cycle count.
* `ADWT`: Adapter wattage?
* `MFNM`, `DENM`, `BTRV`: Battery manufacturer, design energy, revision?
* `BTMD`, `BTTM`: Battery mode/time?

---

## **Thermal Management**

* `TSR1`–`TSR8`: Thermal sensor readings.
* `S3RS`: Possibly a sleep-state restore value or sensor.
* `S3LB`, `S3HB`: S3 state low and high bytes?
* `OSTP`: Overheat setpoint?
* `FULB`, `FUHB`: Fan speed low/high byte?
* `TSEN`, `TPEN`: Touchpad or thermal protection enable?
* `BLOF`: Battery low flag.
* `CRIS`, `CRIL`: Critical state/input/limit?

---

## **Input Devices / Lid / Hotkeys**

* `LID2`, `LIDR`: Lid open/closed state.
* `BKTS`, `EKTS`: Backlight key trigger states?
* `BKLC`: Backlight control?
* `HING`: Hinge state (convertible/tablet mode?)
* `LSTE`: Lid state event?
* `DKIN`, `DKPW`, `DKRS`: Dock status, dock power, dock reset?
* `KBBL`: Keyboard backlight?
* `KBLM`, `KBLS`: Backlight mode/strength.
* `KLED`: Keyboard LED?
* `KBTP`: Keyboard temperature sensor?

---

## **System Modes / Flags**

* `SMAF`, `S4RF`, `ISTD`, `IAQM`, `IAPM`: Sleep mode flags, state flags.
* `TXLK`: Touchpad lock?
* `ECUP`: EC update in progress?
* `FNSP`: Fn key state?
* `NOVB`: No VBIOS? (e.g. graphics related flag)
* `FNRV`: Fn row value?
* `AOUF`: Audio Output flag?
* `GFXF`: Graphics function?
* `ITSM`: IT subsystem mode (bitfield).
* `ITSC`: IT subsystem control?

---

## **SMBus / EC Command Infrastructure**

* `SMPT`, `SMST`, `SMAD`, `SMCD`, `SMDA`: SMBus protocol, status, address, command, data buffer (common naming for EC-I2C transfers).
* `SMD1`, `SMD2`: SMBus Data register(s).
* `SMAA`: SMBus Alert Address?
* `SMBT`: SMBus timeout?
* `VCMD`, `VDAT`, `VSTA`: Vendor command / status.
* `PMSF`: Power Management Status Flag?

---

## **Backlight, Display, LED, Ambient**

* `DISV`: Display valid?
* `LEMD`: LED Mode?
* `SLSR`: Sleep LED state?
* `PB10`: Power button 1.0?
* `LSK2`: Lid switch key?
* `IDCP`: Identifier/control panel?
* `LDSW`: Lid switch?
* `LESR`: LED state restore?

---

## **Fan/Performance Control**

* `OSTP`, `CRIS`, `CRIL`: Overheat, critical state indicators.
* `PBFU`: Possibly a fan update?
* `A8RV`: Some register/value (bitfield).
* `CTL0`–`CTL7`: Control registers (fan, voltage, etc).
* `MGI*`, `MGO*`: Management input/output (possibly for fan/gpu controls?).
* `SARS`: System alarm reset signal?

---

## **BIOS/EC Versions and Params**

* `ECEC`: EC firmware revision.
* `PAR1`–`PAR7`: BIOS parameter variables.
* `VER1`, `VER2`: Version identifiers.
* `BTFW`: Firmware data or hash?
* `RSV1`, `RSV2`: Reserved bytes.

---

### **Miscellaneous**

* `SBMM`: Possibly a system board model?
* `PMSF`: Platform management system flag.
* `BIPT`, `BOPT`: Battery input/output power thresholds?
* `USDC`, `USGC`: USB state current / general current?
* `BTPE`: Battery thermal protection enable?

