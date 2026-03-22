## 图表类型：垂直方向盒须图 (Boxplot Light Velocity2)

**生成指令**：你现在的任务是生成一个 ECharts 的 `option` 配置。请根据以下骨架代码和数据结构要求，结合用户的实际数据进行填充和修改，生成一份完整的图表配置参数。

### ECharts Option 骨架参考
请基于此结构（已剥离冗长写死的数据）生成配置。不要直接输出此骨架，而是要输出**包含真实数据和完整逻辑**的完整 `option` 对象：

```javascript
option = {
  title: [
    {
      text: 'Michelson-Morley Experiment',
      left: 'center'
    },
    {
      text: 'upper: Q3 + 1.5 * IQR \nlower: Q1 - 1.5 * IQR',
      borderColor: '#999',
      borderWidth: 1,
      textStyle: {
        fontSize: 14
      },
      left: '10%',
      top: '90%'
    }
  ],
  dataset: [
    {
      // prettier-ignore
      source: [
                [ /* 请使用用户的真实数据数组替换此处 */ ],
                [ /* 请使用用户的真实数据数组替换此处 */ ],
                [ /* 请使用用户的真实数据数组替换此处 */ ],
                [ /* 请使用用户的真实数据数组替换此处 */ ],
                [ /* 请使用用户的真实数据数组替换此处 */ ]
            ]
    },
    {
      transform: {
        type: 'boxplot',
        config: {
          itemNameFormatter: function (params) {
            return 'expr ' + params.value;
          }
        }
      }
    },
    {
      fromDatasetIndex: 1,
      fromTransformResult: 1
    }
  ],
  tooltip: {
    trigger: 'item',
    axisPointer: {
      type: 'shadow'
    }
  },
  grid: {
    left: '10%',
    right: '10%',
    bottom: '15%'
  },
  yAxis: {
    type: 'category',
    boundaryGap: true,
    nameGap: 30,
    splitArea: {
      show: false
    },
    splitLine: {
      show: false
    }
  },
  xAxis: {
    type: 'value',
    name: 'km/s minus 299,000',
    splitArea: {
      show: true
    }
  },
  series: [
    {
      name: 'boxplot',
      type: 'boxplot',
      datasetIndex: 1
    },
    {
      name: 'outlier',
      type: 'scatter',
      encode: { x: 1, y: 0 },
      datasetIndex: 2
    }
  ]
};
```

