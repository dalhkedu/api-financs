## API FINANCIAMENTO

Python, Flask

#### Tabela de Financiamento SAC

Método: POST

http://127.0.0.1:5000/financiamentos/sac

- Request

```json
{
  "valor_financiado": "100000",
  "taxa_juros_ano": "8.4",
  "numero_parcela": "A"
}
```

Status Code: 200 OK

- Response

```json
{
  "valor_financiado": 100000.0,
  "taxa_juros_mes": 0.7000000000000001,
  "taxa_juros_ano": 8.4,
  "numero_parcelas": 200,
  "amortizacao": 500.0,
  "juros_parcela": [
    700.0000000000001,
    696.5000000000001,
    693.0000000000001,
    689.5000000000001,
    686.0000000000001,
    682.5000000000001,
    679.0000000000001,
    675.5000000000001,
    672.0000000000001,
    668.5000000000001,
    665.0000000000001,
    661.5000000000001,
    658.0000000000001,
    654.5000000000001,
    651.0000000000001,
    647.5000000000001,
    644.0000000000001,
    640.5000000000001,
    637.0000000000001,
    633.5000000000001,
    630.0000000000001,
    626.5000000000001,
    623.0000000000001,
    619.5000000000001,
    616.0000000000001,
    612.5000000000001,
    609.0000000000001,
    605.5000000000001,
    602.0000000000001,
    598.5000000000001,
    595.0000000000001,
    591.5000000000001,
    588.0000000000001,
    584.5000000000001,
    581.0000000000001,
    577.5000000000001,
    574.0000000000001,
    570.5000000000001,
    567.0000000000001,
    563.5000000000001,
    560.0000000000001,
    556.5000000000001,
    553.0000000000001,
    549.5000000000001,
    546.0000000000001,
    542.5000000000001,
    539.0000000000001,
    535.5000000000001,
    532.0000000000001,
    528.5000000000001,
    525.0000000000001,
    521.5000000000001,
    518.0000000000001,
    514.5000000000001,
    511.00000000000006,
    507.50000000000006,
    504.00000000000006,
    500.50000000000006,
    497.00000000000006,
    493.50000000000006,
    490.00000000000006,
    486.50000000000006,
    483.00000000000006,
    479.50000000000006,
    476.00000000000006,
    472.50000000000006,
    469.00000000000006,
    465.50000000000006,
    462.00000000000006,
    458.50000000000006,
    455.00000000000006,
    451.50000000000006,
    448.00000000000006,
    444.50000000000006,
    441.00000000000006,
    437.50000000000006,
    434.00000000000006,
    430.50000000000006,
    427.00000000000006,
    423.50000000000006,
    420.00000000000006,
    416.50000000000006,
    413.00000000000006,
    409.50000000000006,
    406.00000000000006,
    402.50000000000006,
    399.00000000000006,
    395.50000000000006,
    392.00000000000006,
    388.50000000000006,
    385.00000000000006,
    381.50000000000006,
    378.00000000000006,
    374.50000000000006,
    371.00000000000006,
    367.50000000000006,
    364.00000000000006,
    360.50000000000006,
    357.00000000000006,
    353.50000000000006,
    350.00000000000006,
    346.50000000000006,
    343.00000000000006,
    339.50000000000006,
    336.00000000000006,
    332.50000000000006,
    329.00000000000006,
    325.50000000000006,
    322.00000000000006,
    318.50000000000006,
    315.00000000000006,
    311.50000000000006,
    308.00000000000006,
    304.50000000000006,
    301.00000000000006,
    297.50000000000006,
    294.00000000000006,
    290.50000000000006,
    287.00000000000006,
    283.50000000000006,
    280.00000000000006,
    276.50000000000006,
    273.00000000000006,
    269.50000000000006,
    266.00000000000006,
    262.50000000000006,
    259.00000000000006,
    255.50000000000003,
    252.00000000000003,
    248.50000000000003,
    245.00000000000003,
    241.50000000000003,
    238.00000000000003,
    234.50000000000003,
    231.00000000000003,
    227.50000000000003,
    224.00000000000003,
    220.50000000000003,
    217.00000000000003,
    213.50000000000003,
    210.00000000000003,
    206.50000000000003,
    203.00000000000003,
    199.50000000000003,
    196.00000000000003,
    192.50000000000003,
    189.00000000000003,
    185.50000000000003,
    182.00000000000003,
    178.50000000000003,
    175.00000000000003,
    171.50000000000003,
    168.00000000000003,
    164.50000000000003,
    161.00000000000003,
    157.50000000000003,
    154.00000000000003,
    150.50000000000003,
    147.00000000000003,
    143.50000000000003,
    140.00000000000003,
    136.50000000000003,
    133.00000000000003,
    129.50000000000003,
    126.00000000000001,
    122.50000000000001,
    119.00000000000001,
    115.50000000000001,
    112.00000000000001,
    108.50000000000001,
    105.00000000000001,
    101.50000000000001,
    98.00000000000001,
    94.50000000000001,
    91.00000000000001,
    87.50000000000001,
    84.00000000000001,
    80.50000000000001,
    77.00000000000001,
    73.50000000000001,
    70.00000000000001,
    66.50000000000001,
    63.00000000000001,
    59.50000000000001,
    56.00000000000001,
    52.50000000000001,
    49.00000000000001,
    45.50000000000001,
    42.00000000000001,
    38.50000000000001,
    35.00000000000001,
    31.500000000000004,
    28.000000000000004,
    24.500000000000004,
    21.000000000000004,
    17.500000000000004,
    14.000000000000002,
    10.500000000000002,
    7.000000000000001,
    3.5000000000000004
  ],
  "valor_parcela": [
    1200.0,
    1196.5,
    1193.0,
    1189.5,
    1186.0,
    1182.5,
    1179.0,
    1175.5,
    1172.0,
    1168.5,
    1165.0,
    1161.5,
    1158.0,
    1154.5,
    1151.0,
    1147.5,
    1144.0,
    1140.5,
    1137.0,
    1133.5,
    1130.0,
    1126.5,
    1123.0,
    1119.5,
    1116.0,
    1112.5,
    1109.0,
    1105.5,
    1102.0,
    1098.5,
    1095.0,
    1091.5,
    1088.0,
    1084.5,
    1081.0,
    1077.5,
    1074.0,
    1070.5,
    1067.0,
    1063.5,
    1060.0,
    1056.5,
    1053.0,
    1049.5,
    1046.0,
    1042.5,
    1039.0,
    1035.5,
    1032.0,
    1028.5,
    1025.0,
    1021.5000000000001,
    1018.0000000000001,
    1014.5000000000001,
    1011.0,
    1007.5,
    1004.0,
    1000.5,
    997.0,
    993.5,
    990.0,
    986.5,
    983.0,
    979.5,
    976.0,
    972.5,
    969.0,
    965.5,
    962.0,
    958.5,
    955.0,
    951.5,
    948.0,
    944.5,
    941.0,
    937.5,
    934.0,
    930.5,
    927.0,
    923.5,
    920.0,
    916.5,
    913.0,
    909.5,
    906.0,
    902.5,
    899.0,
    895.5,
    892.0,
    888.5,
    885.0,
    881.5,
    878.0,
    874.5,
    871.0,
    867.5,
    864.0,
    860.5,
    857.0,
    853.5,
    850.0,
    846.5,
    843.0,
    839.5,
    836.0,
    832.5,
    829.0,
    825.5,
    822.0,
    818.5,
    815.0,
    811.5,
    808.0,
    804.5,
    801.0,
    797.5,
    794.0,
    790.5,
    787.0,
    783.5,
    780.0,
    776.5,
    773.0,
    769.5,
    766.0,
    762.5,
    759.0,
    755.5,
    752.0,
    748.5,
    745.0,
    741.5,
    738.0,
    734.5,
    731.0,
    727.5,
    724.0,
    720.5,
    717.0,
    713.5,
    710.0,
    706.5,
    703.0,
    699.5,
    696.0,
    692.5,
    689.0,
    685.5,
    682.0,
    678.5,
    675.0,
    671.5,
    668.0,
    664.5,
    661.0,
    657.5,
    654.0,
    650.5,
    647.0,
    643.5,
    640.0,
    636.5,
    633.0,
    629.5,
    626.0,
    622.5,
    619.0,
    615.5,
    612.0,
    608.5,
    605.0,
    601.5,
    598.0,
    594.5,
    591.0,
    587.5,
    584.0,
    580.5,
    577.0,
    573.5,
    570.0,
    566.5,
    563.0,
    559.5,
    556.0,
    552.5,
    549.0,
    545.5,
    542.0,
    538.5,
    535.0,
    531.5,
    528.0,
    524.5,
    521.0,
    517.5,
    514.0,
    510.5,
    507.0,
    503.5
  ],
  "total_juros": 70350.0,
  "total": 170350.0
}
```