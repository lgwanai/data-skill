## 图表类型：映射为渐变色 (Gradient Mapping)

**生成指令**：你现在的任务是生成一个 ECharts 的 `option` 配置。请根据以下骨架代码和数据结构要求，结合用户的实际数据进行填充和修改，生成一份完整的图表配置参数。

### 外部数据结构分析
该图表需要特定的外部数据结构支撑。以下是下载后的数据结构示例，请将用户的真实数据映射为类似结构：

**数据文件 [/data/asset/data/obama_budget_proposal_2012.json]**:
```json
数据是一个数组 (Array)，共 35 项。单项结构示例：
[
  {
    "value": [
      1226629000,
      null,
      null
    ],
    "name": "Health and Human Services",
    "id": "branch-8",
    "discretion": null,
    "children": [
      {
        "value": [
          1105220000,
          1071808000,
          3.11734937600765
        ],
        "name": "Centers for Medicare and Medicaid Services",
        "id": "leaf-135",
        "discretion": "mandatory"
      },
      {
        "value": [
          34502000,
          34325000,
          0.515659140568103
        ],
        "name": "Administration for Children and Families",
        "id": "leaf-131",
        "discretion": "mandatory"
      },
      {
        "value": [
          31829000,
          30784000,
          3.39462058212059
        ],
        "name": "National Institutes of Health",
        "id": "leaf-127",
        "discretion": "discretionary"
      },
      {
        "value": [
          16180000,
          17334000,
          -6.65743625245183
        ],
        "name": "Administration for Children and Families",
        "id": "leaf-118",
        "discretion": "discretionary"
      },
      {
        "value": [
          7324000,
          6246000,
          17.2590457893051
        ],
        "name": "Centers for Medicare and Medicaid Services",
        "id": "leaf-121",
        "discretion": "discretionary"
      },
      {
        "value": [
          6821000,
          7506000,
          -9.12603250732747
        ],
        "name": "Health Resources and Services Administration",
        "id": "leaf-125",
        "discretion": "discretionary"
      },
      {
        "value": [
          5893000,
          6467000,
          -8.8758311427246
        ],
        "name": "Centers for Disease Control and Prevention",
        "id": "leaf-120",
        "discretion": "discretionary"
      },
      {
        "value": [
          4624000,
          4053000,
          14.0883296323711
        ],
        "name": "Indian Health Services",
        "id": "leaf-126",
        "discretion": "discretionary"
      },
      {
        "value": [
          3387000,
          3431000,
          -1.28242494899447
        ],
        "name": "Substance Abuse and Mental Health Services Administration",
        "id": "leaf-130",
        "discretion": "discretionary"
      },
      {
        "value": [
          2744000,
          2599000,
          5.57906887264332
        ],
        "name": "Food and Drug Administration",
        "id": "leaf-124",
        "discretion": "discretionary"
      },
      {
        "value": [
          2237000,
          1513000,
          47.8519497686715
        ],
        "name": "Administration on Aging",
        "id": "leaf-119",
        "discretion": "discretionary"
      },
      {
        "value": [
          2155000,
          707000,
          204.809052333805
        ],
        "name": "Health Resources and Services Administration",
        "id": "leaf-139",
        "discretion": "mandatory"
      },
      {
        "value": [
          1063000,
          4554000,
          -76.6578831796223
        ],
        "name": "Departmental Management",
        "id": "leaf-123",
        "discretion": "discretionary"
      },
      {
        "value": [
          809000,
          297000,
          172.390572390572
        ],
        "name": "Centers for Disease Control and Prevention",
        "id": "leaf-134",
        "discretion": "mandatory"
      },
      {
        "value": [
          647000,
          610000,
          6.06557377049179
        ],
        "name": "Program Support Center",
        "id": "leaf-143",
        "discretion": "mandatory"
      },
      {
        "value": [
          473000,
          1047000,
          -54.8233046800382
        ],
        "name": "Departmental Management",
        "id": "leaf-137",
        "discretion": "mandatory"
      },
      {
        "value": [
          210000,
          10000,
          2000
        ],
        "name": "Administration on Aging",
        "id": "leaf-132",
        "discretion": "mandatory"
      },
      {
        "value": [
          166000,
          166000,
          0
        ],
        "name": "National Institutes of Health",
        "id": "leaf-141",
        "discretion": "mandatory"
      },
      {
        "value": [
          158000,
          158000,
          0
        ],
        "name": "Indian Health Services",
        "id": "leaf-140",
        "discretion": "mandatory"
      },
      {
        "value": [
          93000,
          20000,
          365
        ],
        "name": "Substance Abuse and Mental Health Services Administration",
        "id": "leaf-144",
        "discretion": "mandatory"
      },
      {
        "value": [
          53000,
          50000,
          6.00000000000001
        ],
        "name": "Office of the Inspector General",
        "id": "leaf-128",
        "discretion": "discretionary"
      },
      {
        "value": [
          39000,
          36000,
          8.33333333333333
        ],
        "name": "Program Support Center",
        "id": "leaf-129",
        "discretion": "discretionary"
      },
      {
        "value": [
          2000,
          2000,
          0
        ],
        "name": "Food and Drug Administration",
        "id": "leaf-138",
        "discretion": "mandatory"
      }
    ]
  },
  {
    "value": [
      818284000,
      null,
      null
    ],
    "name": "Social Security Administration",
    "id": "branch-34",
    "discretion": null,
    "children": [
      {
        "value": [
          808041000,
          744812000,
          8.48925634925324
        ],
        "name": "Social Security Administration",
        "id": "leaf-531",
        "discretion": "mandatory"
      },
      {
        "value": [
          10243000,
          9294000,
          10.2108887454271
        ],
        "name": "Social Security Administration",
        "id": "leaf-530",
        "discretion": "discretionary"
      }
    ]
  }
]
```

### ECharts Option 骨架参考
请基于此结构（已剥离冗长写死的数据）生成配置。不要直接输出此骨架，而是要输出**包含真实数据和完整逻辑**的完整 `option` 对象：

```javascript
myChart.showLoading();
const household_america_2012 = 113616229;
$.get(
  ROOT_PATH + '/data/asset/data/obama_budget_proposal_2012.json',
  function (obama_budget_2012) {
    myChart.hideLoading();
    const visualMin = -100;
    const visualMax = 100;
    const visualMinBound = -40;
    const visualMaxBound = 40;
    convertData(obama_budget_2012);
    function convertData(originList) {
      let min = Infinity;
      let max = -Infinity;
      for (let i = 0; i < originList.length; i++) {
        let node = originList[i];
        if (node) {
          let value = node.value;
          value[2] != null && value[2] < min && (min = value[2]);
          value[2] != null && value[2] > max && (max = value[2]);
        }
      }
      for (let i = 0; i < originList.length; i++) {
        let node = originList[i];
        if (node) {
          let value = node.value;
          // Scale value for visual effect
          if (value[2] != null && value[2] > 0) {
            value[3] = echarts.number.linearMap(
              value[2],
              [0, max],
              [visualMaxBound, visualMax],
              true
            );
          } else if (value[2] != null && value[2] < 0) {
            value[3] = echarts.number.linearMap(
              value[2],
              [min, 0],
              [visualMin, visualMinBound],
              true
            );
          } else {
            value[3] = 0;
          }
          if (!isFinite(value[3])) {
            value[3] = 0;
          }
          if (node.children) {
            convertData(node.children);
          }
        }
      }
    }
    function isValidNumber(num) {
      return num != null && isFinite(num);
    }
    myChart.setOption(
      (option = {
        title: {
          left: 'center',
          text: 'Gradient Mapping',
          subtext: 'Growth > 0: green; Growth < 0: red; Growth = 0: grey'
        },
        tooltip: {
          formatter: function (info) {
            let value = info.value;
            let amount = value[0];
            amount = isValidNumber(amount)
              ? echarts.format.addCommas(amount * 1000) + '$'
              : '-';
            let amount2011 = value[1];
            amount2011 = isValidNumber(amount2011)
              ? echarts.format.addCommas(amount2011 * 1000) + '$'
              : '-';
            let change = value[2];
            change = isValidNumber(change) ? change.toFixed(2) + '%' : '-';
            return [
              '<div class="tooltip-title">' +
                echarts.format.encodeHTML(info.name) +
                '</div>',
              '2012 Amount: &nbsp;&nbsp;' + amount + '<br>',
              '2011 Amount: &nbsp;&nbsp;' + amount2011 + '<br>',
              'Change From 2011: &nbsp;&nbsp;' + change
            ].join('');
          }
        },
        series: [
          {
            name: 'ALL',
            top: 80,
            type: 'treemap',
            label: {
              show: true,
              formatter: '{b}'
            },
            itemStyle: {
              borderColor: 'black'
            },
            visualMin: visualMin,
            visualMax: visualMax,
            visualDimension: 3,
            levels: [
              {
                itemStyle: {
                  borderWidth: 3,
                  borderColor: '#333',
                  gapWidth: 3
                }
              },
              {
                color: ['#942e38', '#aaa', '#269f3c'],
                colorMappingBy: 'value',
                itemStyle: {
                  gapWidth: 1
                }
              }
            ],
            data: obama_budget_2012
          }
        ]
      })
    );
  }
);
```

