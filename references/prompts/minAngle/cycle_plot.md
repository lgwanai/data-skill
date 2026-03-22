## 图表类型：周期图 (Cycle Plot)

**生成指令**：你现在的任务是生成一个 ECharts 的 `option` 配置。请根据以下骨架代码和数据结构要求，结合用户的实际数据进行填充和修改，生成一份完整的图表配置参数。

### ECharts Option 骨架参考
请基于此结构（已剥离冗长写死的数据）生成配置。不要直接输出此骨架，而是要输出**包含真实数据和完整逻辑**的完整 `option` 对象：

```javascript
// prettier-ignore
var rawData = [
    [ /* 请使用用户的真实数据数组替换此处 */ ],
    [ /* 请使用用户的真实数据数组替换此处 */ ],
    [ /* 请使用用户的真实数据数组替换此处 */ ],
    [ /* 请使用用户的真实数据数组替换此处 */ ],
    [ /* 请使用用户的真实数据数组替换此处 */ ],
    [ /* 请使用用户的真实数据数组替换此处 */ ],
    [ /* 请使用用户的真实数据数组替换此处 */ ],
    [ /* 请使用用户的真实数据数组替换此处 */ ],
    [ /* 请使用用户的真实数据数组替换此处 */ ],
    [ /* 请使用用户的真实数据数组替换此处 */ ],
    [ /* 请使用用户的真实数据数组替换此处 */ ]
];
var dataByMonth = [];
// prettier-ignore
var months = [ /* 请使用用户的真实数据数组替换此处 */ ];
rawData.forEach(function (entry, yearIndex) {
  entry.forEach(function (value, index) {
    if (index) {
      var monthIndex = index - 1;
      var monthItem = (dataByMonth[monthIndex] = dataByMonth[monthIndex] || []);
      monthItem[0] = monthIndex;
      monthItem[yearIndex + 1] = value;
    }
  });
});
var averageByMonth = [];
dataByMonth.forEach(function (entry, index) {
  var sum = 0;
  entry.forEach(function (value, index) {
    index && (sum += value);
  });
  averageByMonth.push([index, sum / (entry.length - 1)]);
});
function renderTrendItem(params, api) {
  var categoryIndex = api.value(0);
  var unitBandWidth = (api.size([0, 0])[0] * 0.85) / (rawData.length - 1);
  var points = rawData.map(function (entry, index) {
    var value = api.value(index + 1);
    var point = api.coord([categoryIndex, value]);
    point[0] += unitBandWidth * (index - rawData.length / 2);
    return point;
  });
  return {
    type: 'polyline',
    transition: ['shape'],
    shape: {
      points: points
    },
    style: api.style({
      fill: null,
      stroke: api.visual('color'),
      lineWidth: 2
    })
  };
}
function renderAverageItem(param, api) {
  var bandWidth = api.size([0, 0])[0] * 0.85;
  var point = api.coord([api.value(0), api.value(1)]);
  return {
    type: 'line',
    transition: ['shape'],
    shape: {
      x1: point[0] - bandWidth / 2,
      x2: point[0] + bandWidth / 2,
      y1: point[1],
      y2: point[1]
    },
    style: api.style({
      fill: null,
      stroke: api.visual('color'),
      lineWidth: 2
    })
  };
}
option = {
  tooltip: {},
  title: {
    text: 'Sales Trends by Year within Each Month',
    subtext: 'Sample of Cycle Plot',
    left: 'center'
  },
  legend: {
    top: 70,
    data: ['Trend by year (2002 - 2012)', 'Average']
  },
  dataZoom: [
    {
      type: 'slider',
      labelFormatter: ''
    },
    {
      type: 'inside'
    }
  ],
  grid: {
    bottom: 70,
    top: 120
  },
  xAxis: {
    data: months
  },
  yAxis: {
    boundaryGap: [0, '20%']
  },
  series: [
    {
      type: 'custom',
      name: 'Average',
      renderItem: renderAverageItem,
      encode: {
        x: 0,
        y: 1
      },
      data: averageByMonth
    },
    {
      type: 'custom',
      name: 'Trend by year (2002 - 2012)',
      renderItem: renderTrendItem,
      encode: {
        x: 0,
        y: rawData.map(function (entry, index) {
          return index + 1;
        })
      },
      data: dataByMonth
    }
  ]
};
```

