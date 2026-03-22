## 图表类型：元素周期表 (Periodic Table)

**生成指令**：你现在的任务是生成一个 ECharts 的 `option` 配置。请根据以下骨架代码和数据结构要求，结合用户的实际数据进行填充和修改，生成一份完整的图表配置参数。

### ECharts Option 骨架参考
请基于此结构（已剥离冗长写死的数据）生成配置。不要直接输出此骨架，而是要输出**包含真实数据和完整逻辑**的完整 `option` 对象：

```javascript
const colors = {
  red: '#f88',
  green: '#8f8',
  blue: '#8bf',
  yellow: '#ff8'
};
option = {
  matrix: {
    x: {
      data: Array.from({ length: 19 }, (_, i) => i + 1 + ''),
      label: {
        show: false
      },
      itemStyle: {
        borderWidth: 0
      },
      dividerLineStyle: {
        width: 0
      }
    },
    y: {
      data: Array.from({ length: 10 }, (_, i) => i + 1 + ''),
      label: {
        show: false
      },
      itemStyle: {
        borderWidth: 0
      },
      dividerLineStyle: {
        width: 0
      }
    },
    left: 'center',
    width: 900,
    backgroundStyle: {
      borderWidth: 0
    },
    body: {
      itemStyle: {
        borderWidth: 0
      }
    }
  },
  series: {
    type: 'custom',
    coordinateSystem: 'matrix',
    data: [ /* 请使用用户的真实数据数组替换此处 */ ],
    label: {
      show: true,
      formatter: (params) => {
        if (params.value[2] == null) {
          return '{small|' + params.value[3] + '}';
        }
        return params.value[2] + '\n' + params.value[3];
      },
      rich: {
        small: {
          fontSize: 12,
          color: '#777'
        }
      },
      textStyle: {
        fontSize: 14,
        color: '#555',
        align: 'center'
      }
    },
    renderItem: function (params, api) {
      const x = api.value(0);
      const y = api.value(1);
      const rect = api.layout([x, y]).rect;
      const isElement = !isNaN(api.value(2));
      const margin = 2;
      return {
        type: 'rect',
        shape: {
          x: rect.x + margin,
          y: rect.y + margin,
          width: rect.width - margin * 2,
          height: rect.height - margin * 2
        },
        style: api.style({
          fill: api.value(4),
          stroke: '#aaa',
          lineWidth: isElement ? 1 : 0,
          opacity: isElement ? 1 : 0.5
        })
      };
    }
  }
};
setTimeout(function () {
  const elements = [
    ['2', '9', 'Lanthanides', 20],
    ['2', '10', 'Actinides', 20],
    ['1', '1', 'Nonmetals', -70],
    ['1', '2', 'Metals', -70],
    ['19', '1', 'Noble gases', 0, -40],
    ['9', '3', 'Transition metals\n(somtimes excl. group 12)', -25],
    ['1', '8', 's-block\n(incl. He)', 20, -3],
    ['3', '8', 'f-block', 0, -10],
    ['9', '8', 'd-block', -25, -10],
    ['17', '8', 'p-block (excl. He)', -25, -10],
    [
      '16',
      '1',
      'Some elements near\nthe dashed staircase are\nsometimes called metalloids'
    ]
  ].map((row) => {
    const center = myChart.convertToPixel(
      {
        matrixIndex: 0
      },
      row.slice(0, 2)
    );
    return {
      type: 'text',
      style: {
        text: row[2],
        fill: '#333',
        font: 'italic bold 14px sans-serif',
        textAlign: 'center',
        textVerticalAlign: 'middle'
      },
      x: center[0] + (row[3] || 0),
      y: center[1] + (row[4] || 0)
    };
  });
  myChart.setOption({
    graphic: {
      elements
    }
  });
});
```

