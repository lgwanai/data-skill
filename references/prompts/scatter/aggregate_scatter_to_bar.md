## 图表类型：散点图聚合为柱状图动画 (Aggregate Scatter to Bar)

**生成指令**：你现在的任务是生成一个 ECharts 的 `option` 配置。请根据以下骨架代码和数据结构要求，结合用户的实际数据进行填充和修改，生成一份完整的图表配置参数。

### ECharts Option 骨架参考
请基于此结构（已剥离冗长写死的数据）生成配置。不要直接输出此骨架，而是要输出**包含真实数据和完整逻辑**的完整 `option` 对象：

```javascript
// prettier-ignore
const femaleData = [ /* 请使用用户的真实数据数组替换此处 */ ];
// prettier-ignore
const maleDeta = [ /* 请使用用户的真实数据数组替换此处 */ ];
function calculateAverage(data, dim) {
  let total = 0;
  for (var i = 0; i < data.length; i++) {
    total += data[i][dim];
  }
  return (total /= data.length);
}
const scatterOption = (option = {
  xAxis: {
    scale: true
  },
  yAxis: {
    scale: true
  },
  series: [
    {
      type: 'scatter',
      id: 'female',
      dataGroupId: 'female',
      universalTransition: {
        enabled: true,
        delay: function (idx, count) {
          return Math.random() * 400;
        }
      },
      data: femaleData
    },
    {
      type: 'scatter',
      id: 'male',
      dataGroupId: 'male',
      universalTransition: {
        enabled: true,
        delay: function (idx, count) {
          return Math.random() * 400;
        }
      },
      data: maleDeta
    }
  ]
});
const barOption = {
  xAxis: {
    type: 'category',
    data: ['Female', 'Male']
  },
  yAxis: {},
  series: [
    {
      type: 'bar',
      id: 'total',
      data: [
        {
          value: calculateAverage(maleDeta, 0),
          groupId: 'male'
        },
        {
          value: calculateAverage(femaleData, 0),
          groupId: 'female'
        }
      ],
      universalTransition: {
        enabled: true,
        seriesKey: ['female', 'male'],
        delay: function (idx, count) {
          return Math.random() * 400;
        }
      }
    }
  ]
};
let currentOption = scatterOption;
setInterval(function () {
  currentOption = currentOption === scatterOption ? barOption : scatterOption;
  myChart.setOption(currentOption, true);
}, 2000);
```

