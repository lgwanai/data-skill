## 图表类型：农历日历图 (Calendar Lunar)

**生成指令**：你现在的任务是生成一个 ECharts 的 `option` 配置。请根据以下骨架代码和数据结构要求，结合用户的实际数据进行填充和修改，生成一份完整的图表配置参数。

### ECharts Option 骨架参考
请基于此结构（已剥离冗长写死的数据）生成配置。不要直接输出此骨架，而是要输出**包含真实数据和完整逻辑**的完整 `option` 对象：

```javascript
const dateList = [ /* 请使用用户的真实数据数组替换此处 */ ];
const heatmapData = [];
const lunarData = [];
for (let i = 0; i < dateList.length; i++) {
  heatmapData.push([dateList[i][0], Math.random() * 300]);
  lunarData.push([dateList[i][0], 1, dateList[i][1], dateList[i][2]]);
}
option = {
  tooltip: {
    formatter: function (params) {
      return '降雨量: ' + params.value[1].toFixed(2);
    }
  },
  visualMap: {
    show: false,
    min: 0,
    max: 300,
    calculable: true,
    seriesIndex: [2],
    orient: 'horizontal',
    left: 'center',
    bottom: 20,
    inRange: {
      color: ['#e0ffff', '#006edd'],
      opacity: 0.3
    },
    controller: {
      inRange: {
        opacity: 0.5
      }
    }
  },
  calendar: [
    {
      left: 'center',
      top: 'middle',
      cellSize: [70, 70],
      yearLabel: { show: false },
      orient: 'vertical',
      dayLabel: {
        firstDay: 1,
        nameMap: 'cn'
      },
      monthLabel: {
        show: false
      },
      range: '2017-03'
    }
  ],
  series: [
    {
      type: 'scatter',
      coordinateSystem: 'calendar',
      symbolSize: 0,
      label: {
        show: true,
        formatter: function (params) {
          var d = echarts.number.parseDate(params.value[0]);
          return d.getDate() + '\n\n' + params.value[2] + '\n\n';
        },
        color: '#000'
      },
      data: lunarData,
      silent: true
    },
    {
      type: 'scatter',
      coordinateSystem: 'calendar',
      symbolSize: 0,
      label: {
        show: true,
        formatter: function (params) {
          return '\n\n\n' + (params.value[3] || '');
        },
        fontSize: 14,
        fontWeight: 700,
        color: '#a00'
      },
      data: lunarData,
      silent: true
    },
    {
      name: '降雨量',
      type: 'heatmap',
      coordinateSystem: 'calendar',
      data: heatmapData
    }
  ]
};
```

