## 图表类型：默认 encode 设置 (Default arrangement)

**生成指令**：你现在的任务是生成一个 ECharts 的 `option` 配置。请根据以下骨架代码和数据结构要求，结合用户的实际数据进行填充和修改，生成一份完整的图表配置参数。

### ECharts Option 骨架参考
请基于此结构（已剥离冗长写死的数据）生成配置。不要直接输出此骨架，而是要输出**包含真实数据和完整逻辑**的完整 `option` 对象：

```javascript
option = {
  legend: {},
  tooltip: {},
  dataset: {
    source: [
      [ /* 请使用用户的真实数据数组替换此处 */ ],
      [ /* 请使用用户的真实数据数组替换此处 */ ],
      [ /* 请使用用户的真实数据数组替换此处 */ ],
      [ /* 请使用用户的真实数据数组替换此处 */ ],
      [ /* 请使用用户的真实数据数组替换此处 */ ]
    ]
  },
  series: [
    {
      type: 'pie',
      radius: '20%',
      center: ['25%', '30%']
      // No encode specified, by default, it is '2012'.
    },
    {
      type: 'pie',
      radius: '20%',
      center: ['75%', '30%'],
      encode: {
        itemName: 'product',
        value: '2013'
      }
    },
    {
      type: 'pie',
      radius: '20%',
      center: ['25%', '75%'],
      encode: {
        itemName: 'product',
        value: '2014'
      }
    },
    {
      type: 'pie',
      radius: '20%',
      center: ['75%', '75%'],
      encode: {
        itemName: 'product',
        value: '2015'
      }
    }
  ]
};
```

