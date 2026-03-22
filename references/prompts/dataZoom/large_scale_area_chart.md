## 图表类型：大数据量面积图 (Large scale area chart)

**生成指令**：你现在的任务是生成一个 ECharts 的 `option` 配置。请根据以下骨架代码和数据结构要求，结合用户的实际数据进行填充和修改，生成一份完整的图表配置参数。

### ECharts Option 骨架参考
请基于此结构（已剥离冗长写死的数据）生成配置。不要直接输出此骨架，而是要输出**包含真实数据和完整逻辑**的完整 `option` 对象：

```javascript
let base = +new Date(1968, 9, 3);
let oneDay = 24 * 3600 * 1000;
let date = [];
let data = [Math.random() * 300];
for (let i = 1; i < 20000; i++) {
  var now = new Date((base += oneDay));
  date.push([now.getFullYear(), now.getMonth() + 1, now.getDate()].join('/'));
  data.push(Math.round((Math.random() - 0.5) * 20 + data[i - 1]));
}
option = {
  tooltip: {
    trigger: 'axis',
    position: function (pt) {
      return [pt[0], '10%'];
    }
  },
  title: {
    left: 'center',
    text: 'Large Area Chart'
  },
  toolbox: {
    feature: {
      dataZoom: {
        yAxisIndex: 'none'
      },
      restore: {},
      saveAsImage: {}
    }
  },
  xAxis: {
    type: 'category',
    boundaryGap: false,
    data: date
  },
  yAxis: {
    type: 'value',
    boundaryGap: [0, '100%']
  },
  dataZoom: [
    {
      type: 'inside',
      start: 0,
      end: 10
    },
    {
      start: 0,
      end: 10
    }
  ],
  series: [
    {
      name: 'Fake Data',
      type: 'line',
      symbol: 'none',
      sampling: 'lttb',
      itemStyle: {
        color: 'rgb(255, 70, 131)'
      },
      areaStyle: {
        color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
          {
            offset: 0,
            color: 'rgb(255, 158, 68)'
          },
          {
            offset: 1,
            color: 'rgb(255, 70, 131)'
          }
        ])
      },
      data: data
    }
  ]
};
```

