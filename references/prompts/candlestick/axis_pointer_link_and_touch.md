## 图表类型：触屏上的坐标轴指示器 (Axis Pointer Link and Touch)

**生成指令**：你现在的任务是生成一个 ECharts 的 `option` 配置。请根据以下骨架代码和数据结构要求，结合用户的实际数据进行填充和修改，生成一份完整的图表配置参数。

### ECharts Option 骨架参考
请基于此结构（已剥离冗长写死的数据）生成配置。不要直接输出此骨架，而是要输出**包含真实数据和完整逻辑**的完整 `option` 对象：

```javascript
// prettier-ignore
const rawData = [ /* 请使用用户的真实数据数组替换此处 */ ];
// prettier-ignore
const colorList = [ /* 请使用用户的真实数据数组替换此处 */ ];
const labelFont = 'bold 12px Sans-serif';
function calculateMA(dayCount, data) {
  let result = [];
  for (let i = 0, len = data.length; i < len; i++) {
    if (i < dayCount) {
      result.push('-');
      continue;
    }
    let sum = 0;
    for (let j = 0; j < dayCount; j++) {
      sum += +data[i - j][1];
    }
    result.push((sum / dayCount).toFixed(2));
  }
  return result;
}
// prettier-ignore
const dates = [ /* 请使用用户的真实数据数组替换此处 */ ];
// prettier-ignore
const data = [ /* 请使用用户的真实数据数组替换此处 */ ];
// prettier-ignore
const volumes = [ /* 请使用用户的真实数据数组替换此处 */ ];
const dataMA5 = calculateMA(5, data);
const dataMA10 = calculateMA(10, data);
const dataMA20 = calculateMA(20, data);
option = {
  animation: false,
  color: colorList,
  title: {
    left: 'center',
    text: 'Candlestick on Mobile'
  },
  legend: {
    top: 30,
    data: ['日K', 'MA5', 'MA10', 'MA20', 'MA30']
  },
  tooltip: {
    triggerOn: 'none',
    transitionDuration: 0,
    confine: true,
    borderRadius: 4,
    borderWidth: 1,
    borderColor: '#333',
    backgroundColor: 'rgba(255,255,255,0.9)',
    textStyle: {
      fontSize: 12,
      color: '#333'
    },
    position: function (pos, params, el, elRect, size) {
      const obj = {
        top: 60
      };
      obj[['left', 'right'][+(pos[0] < size.viewSize[0] / 2)]] = 5;
      return obj;
    }
  },
  axisPointer: {
    link: [
      {
        xAxisIndex: [0, 1]
      }
    ]
  },
  dataZoom: [
    {
      type: 'slider',
      xAxisIndex: [0, 1],
      realtime: false,
      start: 20,
      end: 70,
      top: 65,
      height: 20,
      handleIcon:
        'path://M10.7,11.9H9.3c-4.9,0.3-8.8,4.4-8.8,9.4c0,5,3.9,9.1,8.8,9.4h1.3c4.9-0.3,8.8-4.4,8.8-9.4C19.5,16.3,15.6,12.2,10.7,11.9z M13.3,24.4H6.7V23h6.6V24.4z M13.3,19.6H6.7v-1.4h6.6V19.6z',
      handleSize: '120%'
    },
    {
      type: 'inside',
      xAxisIndex: [0, 1],
      start: 40,
      end: 70,
      top: 30,
      height: 20
    }
  ],
  xAxis: [
    {
      type: 'category',
      data: dates,
      boundaryGap: false,
      axisLine: { lineStyle: { color: '#777' } },
      axisLabel: {
        formatter: function (value) {
          return echarts.format.formatTime('MM-dd', value);
        }
      },
      min: 'dataMin',
      max: 'dataMax',
      axisPointer: {
        show: true
      }
    },
    {
      type: 'category',
      gridIndex: 1,
      data: dates,
      boundaryGap: false,
      splitLine: { show: false },
      axisLabel: { show: false },
      axisTick: { show: false },
      axisLine: { lineStyle: { color: '#777' } },
      min: 'dataMin',
      max: 'dataMax',
      axisPointer: {
        type: 'shadow',
        label: { show: false },
        triggerTooltip: true,
        handle: {
          show: true,
          margin: 30,
          color: '#B80C00'
        }
      }
    }
  ],
  yAxis: [
    {
      scale: true,
      splitNumber: 2,
      axisLine: { lineStyle: { color: '#777' } },
      splitLine: { show: true },
      axisTick: { show: false },
      axisLabel: {
        inside: true,
        formatter: '{value}\n'
      }
    },
    {
      scale: true,
      gridIndex: 1,
      splitNumber: 2,
      axisLabel: { show: false },
      axisLine: { show: false },
      axisTick: { show: false },
      splitLine: { show: false }
    }
  ],
  grid: [
    {
      left: 20,
      right: 20,
      top: 110,
      height: 120
    },
    {
      left: 20,
      right: 20,
      height: 40,
      top: 260
    }
  ],
  graphic: [
    {
      type: 'group',
      left: 'center',
      top: 70,
      width: 300,
      bounding: 'raw',
      children: [
        {
          id: 'MA5',
          type: 'text',
          style: { fill: colorList[1], font: labelFont },
          left: 0
        },
        {
          id: 'MA10',
          type: 'text',
          style: { fill: colorList[2], font: labelFont },
          left: 'center'
        },
        {
          id: 'MA20',
          type: 'text',
          style: { fill: colorList[3], font: labelFont },
          right: 0
        }
      ]
    }
  ],
  series: [
    {
      name: 'Volume',
      type: 'bar',
      xAxisIndex: 1,
      yAxisIndex: 1,
      itemStyle: {
        color: '#7fbe9e'
      },
      emphasis: {
        itemStyle: {
          color: '#140'
        }
      },
      data: volumes
    },
    {
      type: 'candlestick',
      name: '日K',
      data: data,
      itemStyle: {
        color: '#ef232a',
        color0: '#14b143',
        borderColor: '#ef232a',
        borderColor0: '#14b143'
      },
      emphasis: {
        itemStyle: {
          color: 'black',
          color0: '#444',
          borderColor: 'black',
          borderColor0: '#444'
        }
      }
    },
    {
      name: 'MA5',
      type: 'line',
      data: dataMA5,
      smooth: true,
      showSymbol: false,
      lineStyle: {
        width: 1
      }
    },
    {
      name: 'MA10',
      type: 'line',
      data: dataMA10,
      smooth: true,
      showSymbol: false,
      lineStyle: {
        width: 1
      }
    },
    {
      name: 'MA20',
      type: 'line',
      data: dataMA20,
      smooth: true,
      showSymbol: false,
      lineStyle: {
        width: 1
      }
    }
  ]
};
```

