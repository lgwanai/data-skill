## 图表类型：浏览器占比变化 (Proportion of Browsers)

**生成指令**：你现在的任务是生成一个 ECharts 的 `option` 配置。请根据以下骨架代码和数据结构要求，结合用户的实际数据进行填充和修改，生成一份完整的图表配置参数。

### ECharts Option 骨架参考
请基于此结构（已剥离冗长写死的数据）生成配置。不要直接输出此骨架，而是要输出**包含真实数据和完整逻辑**的完整 `option` 对象：

```javascript
option = {
  title: {
    text: 'Proportion of Browsers',
    subtext: 'Fake Data',
    top: 10,
    left: 10
  },
  tooltip: {
    trigger: 'item'
  },
  legend: {
    type: 'scroll',
    bottom: 10,
    data: (function () {
      var list = [];
      for (var i = 1; i <= 28; i++) {
        list.push(i + 2000 + '');
      }
      return list;
    })()
  },
  visualMap: {
    top: 'middle',
    right: 10,
    inRange: {
      color: ['red', 'yellow']
    },
    calculable: true
  },
  radar: {
    indicator: [
      { text: 'IE8-', max: 400 },
      { text: 'IE9+', max: 400 },
      { text: 'Safari', max: 400 },
      { text: 'Firefox', max: 400 },
      { text: 'Chrome', max: 400 }
    ]
  },
  series: (function () {
    var series = [];
    for (var i = 1; i <= 28; i++) {
      series.push({
        type: 'radar',
        symbol: 'none',
        lineStyle: {
          width: 1
        },
        emphasis: {
          areaStyle: {
            color: 'rgba(0,250,0,0.3)'
          }
        },
        data: [
          {
            value: [
              (40 - i) * 10,
              (38 - i) * 4 + 60,
              i * 5 + 10,
              i * 9,
              (i * i) / 2
            ],
            name: i + 2000 + ''
          }
        ]
      });
    }
    return series;
  })()
};

```

