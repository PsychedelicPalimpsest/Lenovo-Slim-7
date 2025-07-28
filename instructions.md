## Extracting for your own laptop
<sup> Taken from <a href="https://gist.github.com/startergo/a7fcb3155603443f204f9011ed323b2a">here</a></sup>



### Extract raw data
```
sudo acpidump > acpi.log
```

### Extract files
```
acpixtract acpi.log
```


### Disassemble tables
```
iasl -e ssdt1.dat ssdt2.dat ssdt3.dat ssdt4.dat ssdt5.dat ssdt6.dat ssdt7.dat ssdt8.dat -d dsdt.dat
iasl -e dsdt.dat ssdt2.dat ssdt3.dat ssdt4.dat ssdt5.dat ssdt6.dat ssdt7.dat ssdt8.dat -d ssdt1.dat
iasl -e ssdt1.dat dsdt.dat ssdt3.dat ssdt4.dat ssdt5.dat ssdt6.dat ssdt7.dat ssdt8.dat -d ssdt2.dat
iasl -e ssdt1.dat ssdt2.dat dsdt.dat ssdt4.dat ssdt5.dat ssdt6.dat ssdt7.dat ssdt8.dat -d ssdt3.dat
iasl -e ssdt1.dat ssdt2.dat dsdt.dat ssdt3.dat ssdt5.dat ssdt6.dat ssdt7.dat ssdt8.dat -d ssdt4.dat
iasl -e ssdt1.dat ssdt2.dat dsdt.dat ssdt4.dat ssdt3.dat ssdt6.dat ssdt7.dat ssdt8.dat -d ssdt5.dat
iasl -e ssdt1.dat ssdt2.dat dsdt.dat ssdt4.dat ssdt5.dat ssdt3.dat ssdt7.dat ssdt8.dat -d ssdt6.dat
iasl -e ssdt1.dat ssdt2.dat dsdt.dat ssdt4.dat ssdt5.dat ssdt6.dat ssdt3.dat ssdt8.dat -d ssdt7.dat
iasl -e ssdt1.dat ssdt2.dat dsdt.dat ssdt4.dat ssdt5.dat ssdt6.dat ssdt7.dat ssdt3.dat -d ssdt8.dat
```

## Take EcRam dumps to collect info
```
sudo ectool -d
```
Then you start diffing them with ecdiff.py (Edit the file yourself, see the bottom)

