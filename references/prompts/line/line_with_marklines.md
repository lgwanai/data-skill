## 图表类型：折线图的标记线 (Line with Marklines)

**生成指令**：你现在的任务是生成一个 ECharts 的 `option` 配置。请根据以下骨架代码和数据结构要求，结合用户的实际数据进行填充和修改，生成一份完整的图表配置参数。

### ECharts Option 骨架参考
请基于此结构（已剥离冗长写死的数据）生成配置。不要直接输出此骨架，而是要输出**包含真实数据和完整逻辑**的完整 `option` 对象：

```javascript
const markLine = [];
const positions = [ /* 请使用用户的真实数据数组替换此处 */ ];
for (var i = 0; i < positions.length; ++i) {
  markLine.push({
    name: positions[i],
    yAxis: 1.8 - 0.2 * Math.floor(i / 3),
    label: {
      formatter: '{b}',
      position: positions[i]
    }
  });
  if (positions[i] !== 'middle') {
    const name =
      positions[i] === 'insideMiddle' ? 'insideMiddle / middle' : positions[i];
    markLine.push([
      {
        name: 'start: ' + positions[i],
        coord: [0, 0.3],
        label: {
          formatter: name,
          position: positions[i]
        }
      },
      {
        name: 'end: ' + positions[i],
        coord: [3, 1]
      }
    ]);
  }
}
option = {
  animation: false,
  textStyle: {
    fontSize: 14
  },
  xAxis: {
    data: ['A', 'B', 'C', 'D', 'E'],
    boundaryGap: true,
    splitArea: {
      show: true
    }
  },
  yAxis: {
    max: 2
  },
  series: [
    {
      name: 'line',
      type: 'line',
      stack: 'all',
      symbolSize: 6,
      data: [0.3, 1.4, 1.2, 1, 0.6],
      markLine: {
        data: markLine,
        label: {
          distance: [20, 8]
        }
      }
    }
  ],
  grid: {
    top: 30,
    left: 60,
    right: 60,
    bottom: 40
  }
};
```

