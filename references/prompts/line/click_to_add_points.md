## 图表类型：点击添加折线图拐点 (Click to Add Points)

**生成指令**：你现在的任务是生成一个 ECharts 的 `option` 配置。请根据以下骨架代码和数据结构要求，结合用户的实际数据进行填充和修改，生成一份完整的图表配置参数。

### ECharts Option 骨架参考
请基于此结构（已剥离冗长写死的数据）生成配置。不要直接输出此骨架，而是要输出**包含真实数据和完整逻辑**的完整 `option` 对象：

```javascript
const symbolSize = 20;
const data = [
  [15, 0],
  [-50, 10],
  [-56.5, 20],
  [-46.5, 30],
  [-22.1, 40]
];
option = {
  title: {
    text: 'Click to Add Points'
  },
  tooltip: {
    formatter: function (params) {
      var data = params.data || [0, 0];
      return data[0].toFixed(2) + ', ' + data[1].toFixed(2);
    }
  },
  grid: {
    left: '3%',
    right: '4%',
    bottom: '3%',
    containLabel: true
  },
  xAxis: {
    min: -60,
    max: 20,
    type: 'value',
    axisLine: { onZero: false }
  },
  yAxis: {
    min: 0,
    max: 40,
    type: 'value',
    axisLine: { onZero: false }
  },
  series: [
    {
      id: 'a',
      type: 'line',
      smooth: true,
      symbolSize: symbolSize,
      data: data
    }
  ]
};
var zr = myChart.getZr();
zr.on('click', function (params) {
  var pointInPixel = [params.offsetX, params.offsetY];
  var pointInGrid = myChart.convertFromPixel('grid', pointInPixel);
  if (myChart.containPixel('grid', pointInPixel)) {
    data.push(pointInGrid);
    myChart.setOption({
      series: [
        {
          id: 'a',
          data: data
        }
      ]
    });
  }
});
zr.on('mousemove', function (params) {
  var pointInPixel = [params.offsetX, params.offsetY];
  zr.setCursorStyle(
    myChart.containPixel('grid', pointInPixel) ? 'copy' : 'default'
  );
});
```

