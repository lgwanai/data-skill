## 图表类型：简单的矩阵图 (Simple Matrix)

**生成指令**：你现在的任务是生成一个 ECharts 的 `option` 配置。请根据以下骨架代码和数据结构要求，结合用户的实际数据进行填充和修改，生成一份完整的图表配置参数。

### ECharts Option 骨架参考
请基于此结构（已剥离冗长写死的数据）生成配置。不要直接输出此骨架，而是要输出**包含真实数据和完整逻辑**的完整 `option` 对象：

```javascript
option = {
  matrix: {
    x: {
      data: [
        {
          value: 'A',
          children: [
            'A1',
            'A2',
            {
              value: 'A3',
              children: ['A31', 'A32']
            }
          ]
        }
      ]
    },
    y: {
      data: ['U', 'V']
    },
    top: 150,
    bottom: 150
  },
  visualMap: {
    type: 'continuous',
    min: 0,
    max: 80,
    top: 'middle',
    dimension: 2,
    calculable: true
  },
  series: {
    type: 'heatmap',
    coordinateSystem: 'matrix',
    data: [
      ['A1', 'U', 10],
      ['A1', 'V', 20],
      ['A2', 'U', 30],
      ['A2', 'V', 40],
      ['A31', 'U', 50],
      ['A3', 'V', 60]
    ],
    label: {
      show: true
    }
  }
};
```

