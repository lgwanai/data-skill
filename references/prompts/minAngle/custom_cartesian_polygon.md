## 图表类型：自定义多边形图 (Custom Cartesian Polygon)

**生成指令**：你现在的任务是生成一个 ECharts 的 `option` 配置。请根据以下骨架代码和数据结构要求，结合用户的实际数据进行填充和修改，生成一份完整的图表配置参数。

### ECharts Option 骨架参考
请基于此结构（已剥离冗长写死的数据）生成配置。不要直接输出此骨架，而是要输出**包含真实数据和完整逻辑**的完整 `option` 对象：

```javascript
const data = [];
const dataCount = 7;
for (let i = 0; i < dataCount; i++) {
  data.push([
    echarts.number.round(Math.random() * 100),
    echarts.number.round(Math.random() * 400)
  ]);
}
option = {
  tooltip: {
    trigger: 'axis'
  },
  legend: {
    data: ['bar', 'error']
  },
  dataZoom: [
    {
      type: 'slider',
      filterMode: 'none'
    },
    {
      type: 'inside',
      filterMode: 'none'
    }
  ],
  xAxis: {},
  yAxis: {},
  series: [
    {
      type: 'custom',
      renderItem: function (params, api) {
        if (params.context.rendered) {
          return;
        }
        params.context.rendered = true;
        let points = [];
        for (let i = 0; i < data.length; i++) {
          points.push(api.coord(data[i]));
        }
        let color = api.visual('color');
        return {
          type: 'polygon',
          transition: ['shape'],
          shape: {
            points: points
          },
          style: api.style({
            fill: color,
            stroke: echarts.color.lift(color, 0.1)
          })
        };
      },
      clip: true,
      data: data
    }
  ]
};
```

