## 图表类型：混淆矩阵 (Confusion Matrix)

**生成指令**：你现在的任务是生成一个 ECharts 的 `option` 配置。请根据以下骨架代码和数据结构要求，结合用户的实际数据进行填充和修改，生成一份完整的图表配置参数。

### ECharts Option 骨架参考
请基于此结构（已剥离冗长写死的数据）生成配置。不要直接输出此骨架，而是要输出**包含真实数据和完整逻辑**的完整 `option` 对象：

```javascript
const label = {
  fontSize: 16,
  color: '#555'
};
option = {
  matrix: {
    x: {
      data: ['Positive', 'Negative'],
      label
    },
    y: {
      data: ['Positive', 'Negative'],
      label
    },
    top: 80,
    width: 600,
    left: 'center'
  },
  series: {
    type: 'custom',
    coordinateSystem: 'matrix',
    data: [
      ['Positive', 'Positive', 10],
      ['Positive', 'Negative', 2],
      ['Negative', 'Positive', 3],
      ['Negative', 'Negative', 5]
    ],
    label: {
      show: true,
      formatter: (params) => {
        const value = params.value[2];
        return (
          '{name|' +
          (params.value[0] === params.value[1] ? 'True ' : 'False ') +
          params.value[1] +
          '}\n{value|' +
          value +
          '}'
        );
      },
      rich: {
        name: {
          color: '#fff',
          backgroundColor: '#999',
          textBorderColor: '#333',
          padding: 5,
          fontSize: 18
        },
        value: {
          color: '#444',
          textBorderWidth: 0,
          padding: 5,
          fontSize: 16,
          align: 'center'
        }
      }
    },
    renderItem: function (params, api) {
      const x = api.value(0);
      const y = api.value(1);
      const rect = api.layout([x, y]).rect;
      return {
        type: 'rect',
        shape: {
          x: rect.x,
          y: rect.y,
          width: rect.width,
          height: rect.height
        },
        style: api.style({
          fill: x === y ? '#8f8' : '#f88'
        })
      };
    }
  },
  graphic: {
    elements: [
      {
        type: 'text',
        style: {
          text: 'True Class',
          fill: '#333',
          font: 'bold 24px serif',
          textAlign: 'center'
        },
        x: (window.innerWidth - 600) / 2 + (600 / 6) * 4,
        y: 40
      },
      {
        type: 'text',
        style: {
          text: 'Predicted Class',
          fill: '#333',
          font: 'bold 24px serif',
          textAlign: 'center'
        },
        x: (window.innerWidth - 600) / 2 - 50,
        y: 270,
        rotation: Math.PI / 2
      }
    ]
  }
};
```

