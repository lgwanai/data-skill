## 图表类型：男性女性身高体重分布 (Distribution of Height and Weight)

**生成指令**：你现在的任务是生成一个 ECharts 的 `option` 配置。请根据以下骨架代码和数据结构要求，结合用户的实际数据进行填充和修改，生成一份完整的图表配置参数。

### ECharts Option 骨架参考
请基于此结构（已剥离冗长写死的数据）生成配置。不要直接输出此骨架，而是要输出**包含真实数据和完整逻辑**的完整 `option` 对象：

```javascript
option = {
  title: {
    text: 'Male and female height and weight distribution',
    subtext: 'Data from: Heinz 2003'
  },
  grid: {
    left: '3%',
    right: '7%',
    bottom: '7%',
    containLabel: true
  },
  tooltip: {
    // trigger: 'axis',
    showDelay: 0,
    formatter: function (params) {
      if (params.value.length > 1) {
        return (
          params.seriesName +
          ' :<br/>' +
          params.value[0] +
          'cm ' +
          params.value[1] +
          'kg '
        );
      } else {
        return (
          params.seriesName +
          ' :<br/>' +
          params.name +
          ' : ' +
          params.value +
          'kg '
        );
      }
    },
    axisPointer: {
      show: true,
      type: 'cross',
      lineStyle: {
        type: 'dashed',
        width: 1
      }
    }
  },
  toolbox: {
    feature: {
      dataZoom: {},
      brush: {
        type: ['rect', 'polygon', 'clear']
      }
    }
  },
  brush: {},
  legend: {
    data: ['Female', 'Male'],
    left: 'center',
    bottom: 10
  },
  xAxis: [
    {
      type: 'value',
      scale: true,
      axisLabel: {
        formatter: '{value} cm'
      },
      splitLine: {
        show: false
      }
    }
  ],
  yAxis: [
    {
      type: 'value',
      scale: true,
      axisLabel: {
        formatter: '{value} kg'
      },
      splitLine: {
        show: false
      }
    }
  ],
  series: [
    {
      name: 'Female',
      type: 'scatter',
      emphasis: {
        focus: 'series'
      },
      // prettier-ignore
      data: [ /* 请使用用户的真实数据数组替换此处 */ ],
      markArea: {
        silent: true,
        itemStyle: {
          color: 'transparent',
          borderWidth: 1,
          borderType: 'dashed'
        },
        data: [
          [
            {
              name: 'Female Data Range',
              xAxis: 'min',
              yAxis: 'min'
            },
            {
              xAxis: 'max',
              yAxis: 'max'
            }
          ]
        ]
      },
      markPoint: {
        data: [
          { type: 'max', name: 'Max' },
          { type: 'min', name: 'Min' }
        ]
      },
      markLine: {
        lineStyle: {
          type: 'solid'
        },
        data: [{ type: 'average', name: 'AVG' }, { xAxis: 160 }]
      }
    },
    {
      name: 'Male',
      type: 'scatter',
      emphasis: {
        focus: 'series'
      },
      // prettier-ignore
      data: [ /* 请使用用户的真实数据数组替换此处 */ ],
      markArea: {
        silent: true,
        itemStyle: {
          color: 'transparent',
          borderWidth: 1,
          borderType: 'dashed'
        },
        data: [
          [
            {
              name: 'Male Data Range',
              xAxis: 'min',
              yAxis: 'min'
            },
            {
              xAxis: 'max',
              yAxis: 'max'
            }
          ]
        ]
      },
      markPoint: {
        data: [
          { type: 'max', name: 'Max' },
          { type: 'min', name: 'Min' }
        ]
      },
      markLine: {
        lineStyle: {
          type: 'solid'
        },
        data: [{ type: 'average', name: 'Average' }, { xAxis: 170 }]
      }
    }
  ]
};
```

