## 图表类型：相关矩阵（散点图） (Correlation Matrix (Scatter))

**生成指令**：你现在的任务是生成一个 ECharts 的 `option` 配置。请根据以下骨架代码和数据结构要求，结合用户的实际数据进行填充和修改，生成一份完整的图表配置参数。

### ECharts Option 骨架参考
请基于此结构（已剥离冗长写死的数据）生成配置。不要直接输出此骨架，而是要输出**包含真实数据和完整逻辑**的完整 `option` 对象：

```javascript
const xCnt = 10;
const yCnt = 6;
const xData = [];
const yData = [];
for (let i = 0; i < xCnt; ++i) {
  xData.push({
    value: 'X' + (i + 1)
  });
}
for (let i = 0; i < yCnt; ++i) {
  yData.push({
    value: 'Y' + (i + 1)
  });
}
const data = [];
for (let i = 1; i <= xCnt; ++i) {
  for (let j = 1; j <= yCnt; ++j) {
    data.push(['X' + i, 'Y' + j, Math.random() * 2 - 1]);
  }
}
option = {
  matrix: {
    x: {
      data: xData
    },
    y: {
      data: yData
    },
    top: 80
  },
  visualMap: {
    type: 'continuous',
    min: -1,
    max: 1,
    dimension: 2,
    calculable: true,
    orient: 'horizontal',
    top: 5,
    left: 'center',
    inRange: {
      color: [ /* 请使用用户的真实数据数组替换此处 */ ],
      symbolSize: [15, 40]
    }
  },
  series: {
    type: 'scatter',
    coordinateSystem: 'matrix',
    data,
    itemStyle: {
      opacity: 1
    },
    label: {
      show: true,
      formatter: (params) => params.value[2].toFixed(2)
    }
  }
};
```

