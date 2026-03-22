## 图表类型：嵌套环形图 (Nested Pies)

**生成指令**：你现在的任务是生成一个 ECharts 的 `option` 配置。请根据以下骨架代码和数据结构要求，结合用户的实际数据进行填充和修改，生成一份完整的图表配置参数。

### ECharts Option 骨架参考
请基于此结构（已剥离冗长写死的数据）生成配置。不要直接输出此骨架，而是要输出**包含真实数据和完整逻辑**的完整 `option` 对象：

```javascript
option = {
  tooltip: {
    trigger: 'item',
    formatter: '{a} <br/>{b}: {c} ({d}%)'
  },
  legend: {
    data: [ /* 请使用用户的真实数据数组替换此处 */ ]
  },
  series: [
    {
      name: 'Access From',
      type: 'pie',
      selectedMode: 'single',
      radius: [0, '30%'],
      label: {
        position: 'inner',
        fontSize: 14
      },
      labelLine: {
        show: false
      },
      data: [
        { value: 1548, name: 'Search Engine' },
        { value: 775, name: 'Direct' },
        { value: 679, name: 'Marketing', selected: true }
      ]
    },
    {
      name: 'Access From',
      type: 'pie',
      radius: ['45%', '60%'],
      labelLine: {
        length: 30
      },
      label: {
        formatter: '{a|{a}}{abg|}\n{hr|}\n  {b|{b}：}{c}  {per|{d}%}  ',
        backgroundColor: '#F6F8FC',
        borderColor: '#8C8D8E',
        borderWidth: 1,
        borderRadius: 4,
        rich: {
          a: {
            color: '#6E7079',
            lineHeight: 22,
            align: 'center'
          },
          hr: {
            borderColor: '#8C8D8E',
            width: '100%',
            borderWidth: 1,
            height: 0
          },
          b: {
            color: '#4C5058',
            fontSize: 14,
            fontWeight: 'bold',
            lineHeight: 33
          },
          per: {
            color: '#fff',
            backgroundColor: '#4C5058',
            padding: [3, 4],
            borderRadius: 4
          }
        }
      },
      data: [
        { value: 1048, name: 'Baidu' },
        { value: 335, name: 'Direct' },
        { value: 310, name: 'Email' },
        { value: 251, name: 'Google' },
        { value: 234, name: 'Union Ads' },
        { value: 147, name: 'Bing' },
        { value: 135, name: 'Video Ads' },
        { value: 102, name: 'Others' }
      ]
    }
  ]
};
```

