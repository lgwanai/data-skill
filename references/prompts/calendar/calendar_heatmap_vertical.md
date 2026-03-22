## 图表类型：纵向日历图 (Calendar Heatmap Vertical)

**生成指令**：你现在的任务是生成一个 ECharts 的 `option` 配置。请根据以下骨架代码和数据结构要求，结合用户的实际数据进行填充和修改，生成一份完整的图表配置参数。

### ECharts Option 骨架参考
请基于此结构（已剥离冗长写死的数据）生成配置。不要直接输出此骨架，而是要输出**包含真实数据和完整逻辑**的完整 `option` 对象：

```javascript
function getVirtualData(year) {
  const date = +echarts.time.parse(year + '-01-01');
  const end = +echarts.time.parse(+year + 1 + '-01-01');
  const dayTime = 3600 * 24 * 1000;
  const data = [];
  for (let time = date; time < end; time += dayTime) {
    data.push([
      echarts.time.format(time, '{yyyy}-{MM}-{dd}', false),
      Math.floor(Math.random() * 1000)
    ]);
  }
  return data;
}
option = {
  tooltip: {
    position: 'top',
    formatter: function (p) {
      const format = echarts.time.format(p.data[0], '{yyyy}-{MM}-{dd}', false);
      return format + ': ' + p.data[1];
    }
  },
  visualMap: {
    min: 0,
    max: 1000,
    calculable: true,
    orient: 'vertical',
    left: '670',
    top: 'center'
  },
  calendar: [
    {
      orient: 'vertical',
      range: '2015'
    },
    {
      left: 300,
      orient: 'vertical',
      range: '2016'
    },
    {
      left: 520,
      cellSize: [20, 'auto'],
      bottom: 10,
      orient: 'vertical',
      range: '2017',
      dayLabel: {
        margin: 5
      }
    }
  ],
  series: [
    {
      type: 'heatmap',
      coordinateSystem: 'calendar',
      calendarIndex: 0,
      data: getVirtualData('2015')
    },
    {
      type: 'heatmap',
      coordinateSystem: 'calendar',
      calendarIndex: 1,
      data: getVirtualData('2016')
    },
    {
      type: 'heatmap',
      coordinateSystem: 'calendar',
      calendarIndex: 2,
      data: getVirtualData('2017')
    }
  ]
};
```

