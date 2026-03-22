## 图表类型：极坐标系下的堆叠柱状图 (Stacked Bar Chart on Polar(Radial))

**生成指令**：你现在的任务是生成一个 ECharts 的 `option` 配置。请根据以下骨架代码和数据结构要求，结合用户的实际数据进行填充和修改，生成一份完整的图表配置参数。

### ECharts Option 骨架参考
请基于此结构（已剥离冗长写死的数据）生成配置。不要直接输出此骨架，而是要输出**包含真实数据和完整逻辑**的完整 `option` 对象：

```javascript
option = {
  angleAxis: {
    type: 'category',
    data: [ /* 请使用用户的真实数据数组替换此处 */ ]
  },
  radiusAxis: {},
  polar: {},
  series: [
    {
      type: 'bar',
      data: [ /* 请使用用户的真实数据数组替换此处 */ ],
      coordinateSystem: 'polar',
      name: 'A',
      stack: 'a',
      emphasis: {
        focus: 'series'
      }
    },
    {
      type: 'bar',
      data: [ /* 请使用用户的真实数据数组替换此处 */ ],
      coordinateSystem: 'polar',
      name: 'B',
      stack: 'a',
      emphasis: {
        focus: 'series'
      }
    },
    {
      type: 'bar',
      data: [ /* 请使用用户的真实数据数组替换此处 */ ],
      coordinateSystem: 'polar',
      name: 'C',
      stack: 'a',
      emphasis: {
        focus: 'series'
      }
    }
  ],
  legend: {
    show: true,
    data: ['A', 'B', 'C']
  }
};
```

