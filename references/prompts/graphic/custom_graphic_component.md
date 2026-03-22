## 图表类型：自定义图形组件 (Custom Graphic Component)

**生成指令**：你现在的任务是生成一个 ECharts 的 `option` 配置。请根据以下骨架代码和数据结构要求，结合用户的实际数据进行填充和修改，生成一份完整的图表配置参数。

### ECharts Option 骨架参考
请基于此结构（已剥离冗长写死的数据）生成配置。不要直接输出此骨架，而是要输出**包含真实数据和完整逻辑**的完整 `option` 对象：

```javascript
option = {
  legend: {
    data: ['Altitude (km) vs Temperature (°C)']
  },
  tooltip: {
    trigger: 'axis',
    formatter: 'Temperature : <br/>{b}km : {c}°C'
  },
  grid: {
    left: '3%',
    right: '4%',
    bottom: '3%',
    containLabel: true
  },
  xAxis: {
    type: 'value',
    axisLabel: {
      formatter: '{value} °C'
    }
  },
  yAxis: {
    type: 'category',
    axisLine: { onZero: false },
    axisLabel: {
      formatter: '{value} km'
    },
    boundaryGap: true,
    data: [ /* 请使用用户的真实数据数组替换此处 */ ]
  },
  graphic: [
    {
      type: 'group',
      rotation: Math.PI / 4,
      bounding: 'raw',
      right: 110,
      bottom: 110,
      z: 100,
      children: [
        {
          type: 'rect',
          left: 'center',
          top: 'center',
          z: 100,
          shape: {
            width: 400,
            height: 50
          },
          style: {
            fill: 'rgba(0,0,0,0.3)'
          }
        },
        {
          type: 'text',
          left: 'center',
          top: 'center',
          z: 100,
          style: {
            fill: '#fff',
            text: 'ECHARTS LINE CHART',
            font: 'bold 26px sans-serif'
          }
        }
      ]
    },
    {
      type: 'group',
      left: '10%',
      top: 'center',
      children: [
        {
          type: 'rect',
          z: 100,
          left: 'center',
          top: 'middle',
          shape: {
            width: 240,
            height: 90
          },
          style: {
            fill: '#fff',
            stroke: '#555',
            lineWidth: 1,
            shadowBlur: 8,
            shadowOffsetX: 3,
            shadowOffsetY: 3,
            shadowColor: 'rgba(0,0,0,0.2)'
          }
        },
        {
          type: 'text',
          z: 100,
          left: 'center',
          top: 'middle',
          style: {
            fill: '#333',
            width: 220,
            overflow: 'break',
            text: 'xAxis represents temperature in °C, yAxis represents altitude in km, An image watermark in the upper right, This text block can be placed in any place',
            font: '14px Microsoft YaHei'
          }
        }
      ]
    }
  ],
  series: [
    {
      name: '高度(km)与气温(°C)变化关系',
      type: 'line',
      smooth: true,
      data: [15, -50, -56.5, -46.5, -22.1, -2.5, -27.7, -55.7, -76.5]
    }
  ]
};
```

