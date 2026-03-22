## 图表类型：Lastfm 主题河流图 (ThemeRiver Lastfm)

**生成指令**：你现在的任务是生成一个 ECharts 的 `option` 配置。请根据以下骨架代码和数据结构要求，结合用户的实际数据进行填充和修改，生成一份完整的图表配置参数。

### ECharts Option 骨架参考
请基于此结构（已剥离冗长写死的数据）生成配置。不要直接输出此骨架，而是要输出**包含真实数据和完整逻辑**的完整 `option` 对象：

```javascript
// From https://github.com/jsundram/streamgraph.js/blob/master/examples/data/lastfm.js
let rawData = [ /* 请使用用户的真实数据数组替换此处 */ ];
let labels = [ /* 请使用用户的真实数据数组替换此处 */ ];
let data = [];
for (let i = 0; i < rawData.length; i++) {
  for (let j = 0; j < rawData[i].length; j++) {
    let label = labels[i];
    data.push([j, rawData[i][j], label]);
  }
}
option = {
  singleAxis: {
    max: 'dataMax'
  },
  series: [
    {
      type: 'themeRiver',
      data: data,
      label: {
        show: false
      }
    }
  ]
};
```

