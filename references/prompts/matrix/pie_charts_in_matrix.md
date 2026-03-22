## 图表类型：矩阵布局下的饼图 (Pie Charts in Matrix)

**生成指令**：你现在的任务是生成一个 ECharts 的 `option` 配置。请根据以下骨架代码和数据结构要求，结合用户的实际数据进行填充和修改，生成一份完整的图表配置参数。

### ECharts Option 骨架参考
请基于此结构（已剥离冗长写死的数据）生成配置。不要直接输出此骨架，而是要输出**包含真实数据和完整逻辑**的完整 `option` 对象：

```javascript
const xCnt = 9;
const yCnt = 6;
const series = [];
for (let i = 0; i < xCnt; ++i) {
  for (let j = 0; j < yCnt; ++j) {
    series.push({
      type: 'pie',
      coordinateSystem: 'matrix',
      center: [`Grade ${i + 1}`, `Class ${j + 1}`],
      radius: 18,
      data: [
        {
          value: Math.round(Math.random() * 10) + 10,
          name: 'Male'
        },
        {
          value: Math.round(Math.random() * 10) + 10,
          name: 'Female'
        }
      ],
      label: {
        show: false
      },
      emphasis: {
        label: {
          show: false
        }
      }
    });
  }
}
option = {
  legend: {
    show: true,
    bottom: 40
  },
  matrix: {
    x: {
      data: [
        {
          value: 'Primary School',
          children: Array.from({ length: 5 }, (_, i) => {
            return `Grade ${i + 1}`;
          })
        },
        {
          value: 'High School',
          children: Array.from({ length: 4 }, (_, i) => {
            return `Grade ${i + 6}`;
          })
        }
      ]
    },
    y: {
      data: Array.from({ length: 6 }, (_, i) => {
        return `Class ${i + 1}`;
      })
    },
    top: 80,
    bottom: 80
  },
  series,
  tooltip: {
    show: true
  }
};
```

