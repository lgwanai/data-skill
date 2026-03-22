## 图表类型：极坐标双数值轴 (Two Value-Axes in Polar)

**生成指令**：你现在的任务是生成一个 ECharts 的 `option` 配置。请根据以下骨架代码和数据结构要求，结合用户的实际数据进行填充和修改，生成一份完整的图表配置参数。

### ECharts Option 骨架参考
请基于此结构（已剥离冗长写死的数据）生成配置。不要直接输出此骨架，而是要输出**包含真实数据和完整逻辑**的完整 `option` 对象：

```javascript
const data = [];
for (let i = 0; i <= 360; i++) {
  let t = (i / 180) * Math.PI;
  let r = Math.sin(2 * t) * Math.cos(2 * t);
  data.push([r, i]);
}
option = {
  title: {
    text: 'Two Value-Axes in Polar'
  },
  legend: {
    data: ['line']
  },
  polar: {
    center: ['50%', '54%']
  },
  tooltip: {
    trigger: 'axis',
    axisPointer: {
      type: 'cross'
    }
  },
  angleAxis: {
    type: 'value',
    startAngle: 0
  },
  radiusAxis: {
    min: 0
  },
  series: [
    {
      coordinateSystem: 'polar',
      name: 'line',
      type: 'line',
      showSymbol: false,
      data: data
    }
  ],
  animationDuration: 2000
};
```

