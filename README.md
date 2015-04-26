# AddrToQuadkey
Transfer address to quadkey

### thanks to `https://github.com/buckheroux/QuadKey`

####example data (test/addrList.csv)
```
原燒(台中中港店),台中市西區臺灣大道二段545號
陳家涼麵,台北市松山區南京東路五段123巷29號
成都楊桃冰,台北市萬華區成都路3號
梨子咖啡館,台中市西屯區玉門路370巷28號
```

#### usage

```shell
# plz install quadkey first
pip install quadkey
```

```shell
python addrToQuadkey.py test/addrList.csv test/test2.csv
```

####reault data
```
原燒(台中中港店),台中市西區臺灣大道二段545號,24.15702,120.658781,132123211300310
陳家涼麵,台北市松山區南京東路五段123巷29號,25.0527948,121.5606571,132123122113022
成都楊桃冰,台北市萬華區成都路3號,25.0426559,121.507901,132123122112211
梨子咖啡館,台中市西屯區玉門路370巷28號,24.188835,120.613181,132123211300012
```