## 图表类型：带圆角的堆积柱状图 (Stacked Bar with borderRadius)

**生成指令**：你现在的任务是生成一个 ECharts 的 `option` 配置。请根据以下骨架代码和数据结构要求，结合用户的实际数据进行填充和修改，生成一份完整的图表配置参数。

### ECharts Option 骨架参考
请基于此结构（已剥离冗长写死的数据）生成配置。不要直接输出此骨架，而是要输出**包含真实数据和完整逻辑**的完整 `option` 对象：

```javascript
var series = [
  {
    data: [ /* 请使用用户的真实数据数组替换此处 */ ],
    type: 'bar',
    stack: 'a',
    name: 'a'
  },
  {
    data: [ /* 请使用用户的真实数据数组替换此处 */ ],
    type: 'bar',
    stack: 'a',
    name: 'b'
  },
  {
    data: [ /* 请使用用户的真实数据数组替换此处 */ ],
    type: 'bar',
    stack: 'a',
    name: 'c'
  },
  {
    data: [ /* 请使用用户的真实数据数组替换此处 */ ],
    type: 'bar',
    stack: 'b',
    name: 'd'
  },
  {
    data: [ /* 请使用用户的真实数据数组替换此处 */ ],
    type: 'bar',
    stack: 'b',
    name: 'e'
  }
];
const stackInfo = {};
for (let i = 0; i < series[0].data.length; ++i) {
  for (let j = 0; j < series.length; ++j) {
    const stackName = series[j].stack;
    if (!stackName) {
      continue;
    }
    if (!stackInfo[stackName]) {
      stackInfo[stackName] = {
        stackStart: [],
        stackEnd: []
      };
    }
    const info = stackInfo[stackName];
    const data = series[j].data[i];
    if (data && data !== '-') {
      if (info.stackStart[i] == null) {
        info.stackStart[i] = j;
      }
      info.stackEnd[i] = j;
    }
  }
}
for (let i = 0; i < series.length; ++i) {
  const data = series[i].data;
  const info = stackInfo[series[i].stack];
  for (let j = 0; j < series[i].data.length; ++j) {
    // const isStart = info.stackStart[j] === i;
    const isEnd = info.stackEnd[j] === i;
    const topBorder = isEnd ? 20 : 0;
    const bottomBorder = 0;
    data[j] = {
      value: data[j],
      itemStyle: {
        borderRadius: [topBorder, topBorder, bottomBorder, bottomBorder]
      }
    };
  }
}
option = {
  xAxis: {
    type: 'category',
    data: [ /* 请使用用户的真实数据数组替换此处 */ ]
  },
  yAxis: {
    type: 'value'
  },
  series: series
};
```

