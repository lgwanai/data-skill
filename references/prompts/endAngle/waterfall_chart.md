## 图表类型：阶梯瀑布图（柱状图模拟） (Waterfall Chart)

**生成指令**：你现在的任务是生成一个 ECharts 的 `option` 配置。请根据以下骨架代码和数据结构要求，结合用户的实际数据进行填充和修改，生成一份完整的图表配置参数。

### ECharts Option 骨架参考
请基于此结构（已剥离冗长写死的数据）生成配置。不要直接输出此骨架，而是要输出**包含真实数据和完整逻辑**的完整 `option` 对象：

```javascript
option = {
  title: {
    text: 'Accumulated Waterfall Chart'
  },
  tooltip: {
    trigger: 'axis',
    axisPointer: {
      type: 'shadow'
    },
    formatter: function (params) {
      let tar;
      if (params[1] && params[1].value !== '-') {
        tar = params[1];
      } else {
        tar = params[2];
      }
      return tar && tar.name + '<br/>' + tar.seriesName + ' : ' + tar.value;
    }
  },
  legend: {
    data: ['Expenses', 'Income']
  },
  grid: {
    left: '3%',
    right: '4%',
    bottom: '3%',
    containLabel: true
  },
  xAxis: {
    type: 'category',
    data: (function () {
      let list = [];
      for (let i = 1; i <= 11; i++) {
        list.push('Nov ' + i);
      }
      return list;
    })()
  },
  yAxis: {
    type: 'value'
  },
  series: [
    {
      name: 'Placeholder',
      type: 'bar',
      stack: 'Total',
      silent: true,
      itemStyle: {
        borderColor: 'transparent',
        color: 'transparent'
      },
      emphasis: {
        itemStyle: {
          borderColor: 'transparent',
          color: 'transparent'
        }
      },
      data: [ /* 请使用用户的真实数据数组替换此处 */ ]
    },
    {
      name: 'Income',
      type: 'bar',
      stack: 'Total',
      label: {
        show: true,
        position: 'top'
      },
      data: [ /* 请使用用户的真实数据数组替换此处 */ ]
    },
    {
      name: 'Expenses',
      type: 'bar',
      stack: 'Total',
      label: {
        show: true,
        position: 'bottom'
      },
      data: [ /* 请使用用户的真实数据数组替换此处 */ ]
    }
  ]
};
```

