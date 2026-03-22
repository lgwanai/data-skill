## 图表类型：OHLC 图（使用自定义系列） (OHLC Chart)

**生成指令**：你现在的任务是生成一个 ECharts 的 `option` 配置。请根据以下骨架代码和数据结构要求，结合用户的实际数据进行填充和修改，生成一份完整的图表配置参数。

### 外部数据结构分析
该图表需要特定的外部数据结构支撑。以下是下载后的数据结构示例，请将用户的真实数据映射为类似结构：

**数据文件 [/data/asset/data/stock-DJI.json]**:
```json
数据是一个数组 (Array)，共 3141 项。单项结构示例：
[
  [
    "2004-01-02",
    10452.74,
    10409.85,
    10367.41,
    10554.96,
    168890000
  ],
  [
    "2004-01-05",
    10411.85,
    10544.07,
    10411.85,
    10575.92,
    221290000
  ]
]
```

### ECharts Option 骨架参考
请基于此结构（已剥离冗长写死的数据）生成配置。不要直接输出此骨架，而是要输出**包含真实数据和完整逻辑**的完整 `option` 对象：

```javascript
function splitData(rawData) {
  const categoryData = [];
  const values = [];
  for (var i = 0; i < rawData.length; i++) {
    categoryData.push(rawData[i][0]);
    rawData[i][0] = i;
    values.push(rawData[i]);
  }
  return {
    categoryData: categoryData,
    values: values
  };
}
function renderItem(params, api) {
  var xValue = api.value(0);
  var openPoint = api.coord([xValue, api.value(1)]);
  var closePoint = api.coord([xValue, api.value(2)]);
  var lowPoint = api.coord([xValue, api.value(3)]);
  var highPoint = api.coord([xValue, api.value(4)]);
  var halfWidth = api.size([1, 0])[0] * 0.35;
  var style = api.style({
    stroke: api.visual('color')
  });
  return {
    type: 'group',
    children: [
      {
        type: 'line',
        shape: {
          x1: lowPoint[0],
          y1: lowPoint[1],
          x2: highPoint[0],
          y2: highPoint[1]
        },
        style: style
      },
      {
        type: 'line',
        shape: {
          x1: openPoint[0],
          y1: openPoint[1],
          x2: openPoint[0] - halfWidth,
          y2: openPoint[1]
        },
        style: style
      },
      {
        type: 'line',
        shape: {
          x1: closePoint[0],
          y1: closePoint[1],
          x2: closePoint[0] + halfWidth,
          y2: closePoint[1]
        },
        style: style
      }
    ]
  };
}
$.get(ROOT_PATH + '/data/asset/data/stock-DJI.json', function (rawData) {
  var data = splitData(rawData);
  myChart.setOption(
    (option = {
      animation: false,
      legend: {
        bottom: 10,
        left: 'center',
        data: ['Dow-Jones index']
      },
      tooltip: {
        trigger: 'axis',
        axisPointer: {
          type: 'cross'
        },
        position: function (pos, params, el, elRect, size) {
          var obj = { top: 10 };
          obj[['left', 'right'][+(pos[0] < size.viewSize[0] / 2)]] = 30;
          return obj;
        }
      },
      axisPointer: {
        link: [{ xAxisIndex: 'all' }]
      },
      toolbox: {
        feature: {
          dataZoom: {
            yAxisIndex: false
          },
          brush: {
            type: ['lineX', 'clear']
          }
        }
      },
      grid: [
        {
          left: '10%',
          right: '8%',
          bottom: 150
        }
      ],
      xAxis: [
        {
          type: 'category',
          data: data.categoryData,
          boundaryGap: false,
          axisLine: { onZero: false },
          splitLine: { show: false },
          min: 'dataMin',
          max: 'dataMax',
          axisPointer: {
            z: 100
          }
        }
      ],
      yAxis: [
        {
          scale: true,
          splitArea: {
            show: true
          }
        }
      ],
      dataZoom: [
        {
          type: 'inside',
          start: 98,
          end: 100,
          minValueSpan: 10
        },
        {
          show: true,
          type: 'slider',
          bottom: 60,
          start: 98,
          end: 100,
          minValueSpan: 10
        }
      ],
      series: [
        {
          name: 'Dow-Jones index',
          type: 'custom',
          renderItem: renderItem,
          dimensions: ['-', 'open', 'close', 'lowest', 'highest'],
          encode: {
            x: 0,
            y: [1, 2, 3, 4],
            tooltip: [1, 2, 3, 4]
          },
          data: data.values
        }
      ]
    }),
    true
  );
});
```

