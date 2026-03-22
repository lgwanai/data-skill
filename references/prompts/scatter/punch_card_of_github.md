## 图表类型：GitHub 打卡气泡图（极坐标） (Punch Card of Github)

**生成指令**：你现在的任务是生成一个 ECharts 的 `option` 配置。请根据以下骨架代码和数据结构要求，结合用户的实际数据进行填充和修改，生成一份完整的图表配置参数。

### ECharts Option 骨架参考
请基于此结构（已剥离冗长写死的数据）生成配置。不要直接输出此骨架，而是要输出**包含真实数据和完整逻辑**的完整 `option` 对象：

```javascript
// prettier-ignore
const hours = [ /* 请使用用户的真实数据数组替换此处 */ ];
// prettier-ignore
const days = [ /* 请使用用户的真实数据数组替换此处 */ ];
// prettier-ignore
const data = [ /* 请使用用户的真实数据数组替换此处 */ ];
option = {
  title: {
    text: 'Punch Card of Github'
  },
  legend: {
    data: ['Punch Card'],
    left: 'right'
  },
  polar: {},
  tooltip: {
    formatter: function (params) {
      return (
        params.value[2] +
        ' commits in ' +
        hours[params.value[1]] +
        ' of ' +
        days[params.value[0]]
      );
    }
  },
  angleAxis: {
    type: 'category',
    data: hours,
    boundaryGap: false,
    splitLine: {
      show: true
    },
    axisLine: {
      show: false
    }
  },
  radiusAxis: {
    type: 'category',
    data: days,
    axisLine: {
      show: false
    },
    axisLabel: {
      rotate: 45
    }
  },
  series: [
    {
      name: 'Punch Card',
      type: 'scatter',
      coordinateSystem: 'polar',
      symbolSize: function (val) {
        return val[2] * 2;
      },
      data: data,
      animationDelay: function (idx) {
        return idx * 5;
      }
    }
  ]
};
```

