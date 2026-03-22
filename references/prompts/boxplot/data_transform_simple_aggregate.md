## 图表类型：简单的数据聚合 (Data Transform Simple Aggregate)

**生成指令**：你现在的任务是生成一个 ECharts 的 `option` 配置。请根据以下骨架代码和数据结构要求，结合用户的实际数据进行填充和修改，生成一份完整的图表配置参数。

### 外部数据结构分析
该图表需要特定的外部数据结构支撑。以下是下载后的数据结构示例，请将用户的真实数据映射为类似结构：

**数据文件 [/data/asset/data/life-expectancy-table.json]**:
```json
数据是一个数组 (Array)，共 1540 项。单项结构示例：
[
  [
    "Income",
    "Life Expectancy",
    "Population",
    "Country",
    "Year"
  ],
  [
    815,
    34.05,
    351014,
    "Australia",
    1800
  ]
]
```

### ECharts Option 骨架参考
请基于此结构（已剥离冗长写死的数据）生成配置。不要直接输出此骨架，而是要输出**包含真实数据和完整逻辑**的完整 `option` 对象：

```javascript
$.when(
  $.get(ROOT_PATH + '/data/asset/data/life-expectancy-table.json'),
  $.getScript(
    CDN_PATH + 'echarts-simple-transform/dist/ecSimpleTransform.min.js'
  )
).done(function (res) {
  run(res[0]);
});
function run(_rawData) {
  echarts.registerTransform(ecSimpleTransform.aggregate);
  option = {
    dataset: [
      {
        id: 'raw',
        source: _rawData
      },
      {
        id: 'since_year',
        fromDatasetId: 'raw',
        transform: [
          {
            type: 'filter',
            config: {
              dimension: 'Year',
              gte: 1950
            }
          }
        ]
      },
      {
        id: 'income_aggregate',
        fromDatasetId: 'since_year',
        transform: [
          {
            type: 'ecSimpleTransform:aggregate',
            config: {
              resultDimensions: [
                { name: 'min', from: 'Income', method: 'min' },
                { name: 'Q1', from: 'Income', method: 'Q1' },
                { name: 'median', from: 'Income', method: 'median' },
                { name: 'Q3', from: 'Income', method: 'Q3' },
                { name: 'max', from: 'Income', method: 'max' },
                { name: 'Country', from: 'Country' }
              ],
              groupBy: 'Country'
            }
          },
          {
            type: 'sort',
            config: {
              dimension: 'Q3',
              order: 'asc'
            }
          }
        ]
      }
    ],
    title: {
      text: 'Income since 1950'
    },
    tooltip: {
      trigger: 'axis',
      confine: true
    },
    xAxis: {
      name: 'Income',
      nameLocation: 'middle',
      nameGap: 30,
      scale: true
    },
    yAxis: {
      type: 'category'
    },
    grid: {
      bottom: 140
    },
    legend: {
      selected: { detail: false }
    },
    dataZoom: [
      {
        type: 'inside'
      },
      {
        type: 'slider',
        height: 20,
        bottom: 60
      }
    ],
    series: [
      {
        name: 'boxplot',
        type: 'boxplot',
        datasetId: 'income_aggregate',
        itemStyle: {
          color: '#b8c5f2'
        },
        encode: {
          x: ['min', 'Q1', 'median', 'Q3', 'max'],
          y: 'Country',
          itemName: ['Country'],
          tooltip: ['min', 'Q1', 'median', 'Q3', 'max']
        }
      },
      {
        name: 'detail',
        type: 'scatter',
        datasetId: 'since_year',
        symbolSize: 6,
        tooltip: {
          trigger: 'item'
        },
        label: {
          show: true,
          position: 'top',
          align: 'left',
          verticalAlign: 'middle',
          rotate: 90,
          fontSize: 12
        },
        itemStyle: {
          color: '#d00000'
        },
        encode: {
          x: 'Income',
          y: 'Country',
          label: 'Year',
          itemName: 'Year',
          tooltip: ['Country', 'Year', 'Income']
        }
      }
    ]
  };
  myChart.setOption(option);
}
```

