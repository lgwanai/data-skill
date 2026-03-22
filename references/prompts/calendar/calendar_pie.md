## 图表类型：日历饼图 (Calendar Pie)

**生成指令**：你现在的任务是生成一个 ECharts 的 `option` 配置。请根据以下骨架代码和数据结构要求，结合用户的实际数据进行填充和修改，生成一份完整的图表配置参数。

### ECharts Option 骨架参考
请基于此结构（已剥离冗长写死的数据）生成配置。不要直接输出此骨架，而是要输出**包含真实数据和完整逻辑**的完整 `option` 对象：

```javascript
// This example requires ECharts v5.4.0 or later
const cellSize = [80, 80];
const pieRadius = 30;
function getVirtualData() {
  const date = +echarts.time.parse('2017-02-01');
  const end = +echarts.time.parse('2017-03-01');
  const dayTime = 3600 * 24 * 1000;
  const data = [];
  for (let time = date; time < end; time += dayTime) {
    data.push([
      echarts.time.format(time, '{yyyy}-{MM}-{dd}', false),
      Math.floor(Math.random() * 10000)
    ]);
  }
  return data;
}
const scatterData = getVirtualData();
const pieSeries = scatterData.map(function (item, index) {
  return {
    type: 'pie',
    id: 'pie-' + index,
    center: item[0],
    radius: pieRadius,
    coordinateSystem: 'calendar',
    label: {
      formatter: '{c}',
      position: 'inside'
    },
    data: [
      { name: 'Work', value: Math.round(Math.random() * 24) },
      { name: 'Entertainment', value: Math.round(Math.random() * 24) },
      { name: 'Sleep', value: Math.round(Math.random() * 24) }
    ]
  };
});
option = {
  tooltip: {},
  legend: {
    data: ['Work', 'Entertainment', 'Sleep'],
    bottom: 20
  },
  calendar: {
    top: 'middle',
    left: 'center',
    orient: 'vertical',
    cellSize: cellSize,
    yearLabel: {
      show: false,
      fontSize: 30
    },
    dayLabel: {
      margin: 20,
      firstDay: 1,
      nameMap: [ /* 请使用用户的真实数据数组替换此处 */ ]
    },
    monthLabel: {
      show: false
    },
    range: ['2017-02']
  },
  series: [
    {
      id: 'label',
      type: 'scatter',
      coordinateSystem: 'calendar',
      symbolSize: 0,
      label: {
        show: true,
        formatter: function (params) {
          return echarts.time.format(params.value[0], '{dd}', false);
        },
        offset: [-cellSize[0] / 2 + 10, -cellSize[1] / 2 + 10],
        fontSize: 14
      },
      data: scatterData
    },
    ...pieSeries
  ]
};
```

