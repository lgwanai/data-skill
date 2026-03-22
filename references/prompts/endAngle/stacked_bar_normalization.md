## 图表类型：堆叠柱状图的归一化 (Stacked Bar Normalization)

**生成指令**：你现在的任务是生成一个 ECharts 的 `option` 配置。请根据以下骨架代码和数据结构要求，结合用户的实际数据进行填充和修改，生成一份完整的图表配置参数。

### ECharts Option 骨架参考
请基于此结构（已剥离冗长写死的数据）生成配置。不要直接输出此骨架，而是要输出**包含真实数据和完整逻辑**的完整 `option` 对象：

```javascript
// There should not be negative values in rawData
const rawData = [
  [ /* 请使用用户的真实数据数组替换此处 */ ],
  [ /* 请使用用户的真实数据数组替换此处 */ ],
  [ /* 请使用用户的真实数据数组替换此处 */ ],
  [ /* 请使用用户的真实数据数组替换此处 */ ],
  [ /* 请使用用户的真实数据数组替换此处 */ ]
];
const totalData = [];
for (let i = 0; i < rawData[0].length; ++i) {
  let sum = 0;
  for (let j = 0; j < rawData.length; ++j) {
    sum += rawData[j][i];
  }
  totalData.push(sum);
}
const series = [
  'Direct',
  'Mail Ad',
  'Affiliate Ad',
  'Video Ad',
  'Search Engine'
].map((name, sid) => {
  return {
    name,
    type: 'bar',
    stack: 'total',
    barWidth: '60%',
    label: {
      show: true,
      formatter: (params) => Math.round(params.value * 1000) / 10 + '%'
    },
    data: rawData[sid].map((d, did) =>
      totalData[did] <= 0 ? 0 : d / totalData[did]
    )
  };
});
option = {
  legend: {
    selectedMode: false
  },
  yAxis: {
    type: 'value'
  },
  xAxis: {
    type: 'category',
    data: [ /* 请使用用户的真实数据数组替换此处 */ ]
  },
  series
};
```

