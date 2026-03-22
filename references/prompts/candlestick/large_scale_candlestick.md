## 图表类型：大数据量K线图 (Large Scale Candlestick)

**生成指令**：你现在的任务是生成一个 ECharts 的 `option` 配置。请根据以下骨架代码和数据结构要求，结合用户的实际数据进行填充和修改，生成一份完整的图表配置参数。

### ECharts Option 骨架参考
请基于此结构（已剥离冗长写死的数据）生成配置。不要直接输出此骨架，而是要输出**包含真实数据和完整逻辑**的完整 `option` 对象：

```javascript
const upColor = '#ec0000';
const upBorderColor = '#8A0000';
const downColor = '#00da3c';
const downBorderColor = '#008F28';
const dataCount = 2e5;
const data = generateOHLC(dataCount);
option = {
  dataset: {
    source: data
  },
  title: {
    text: 'Data Amount: ' + echarts.format.addCommas(dataCount)
  },
  tooltip: {
    trigger: 'axis',
    axisPointer: {
      type: 'line'
    }
  },
  toolbox: {
    feature: {
      dataZoom: {
        yAxisIndex: false
      }
    }
  },
  grid: [
    {
      left: '10%',
      right: '10%',
      bottom: 200
    },
    {
      left: '10%',
      right: '10%',
      height: 80,
      bottom: 80
    }
  ],
  xAxis: [
    {
      type: 'category',
      boundaryGap: false,
      // inverse: true,
      axisLine: { onZero: false },
      splitLine: { show: false },
      min: 'dataMin',
      max: 'dataMax'
    },
    {
      type: 'category',
      gridIndex: 1,
      boundaryGap: false,
      axisLine: { onZero: false },
      axisTick: { show: false },
      splitLine: { show: false },
      axisLabel: { show: false },
      min: 'dataMin',
      max: 'dataMax'
    }
  ],
  yAxis: [
    {
      scale: true,
      splitArea: {
        show: true
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
  dataZoom: [
    {
      type: 'inside',
      xAxisIndex: [0, 1],
      start: 10,
      end: 100
    },
    {
      show: true,
      xAxisIndex: [0, 1],
      type: 'slider',
      bottom: 10,
      start: 10,
      end: 100
    }
  ],
  visualMap: {
    show: false,
    seriesIndex: 1,
    dimension: 6,
    pieces: [
      {
        value: 1,
        color: upColor
      },
      {
        value: -1,
        color: downColor
      }
    ]
  },
  series: [
    {
      type: 'candlestick',
      itemStyle: {
        color: upColor,
        color0: downColor,
        borderColor: upBorderColor,
        borderColor0: downBorderColor
      },
      encode: {
        x: 0,
        y: [1, 4, 3, 2]
      }
    },
    {
      name: 'Volumn',
      type: 'bar',
      xAxisIndex: 1,
      yAxisIndex: 1,
      itemStyle: {
        color: '#7fbe9e'
      },
      large: true,
      encode: {
        x: 0,
        y: 5
      }
    }
  ]
};
function generateOHLC(count) {
  let data = [];
  let xValue = +new Date(2011, 0, 1);
  let minute = 60 * 1000;
  let baseValue = Math.random() * 12000;
  let boxVals = new Array(4);
  let dayRange = 12;
  for (let i = 0; i < count; i++) {
    baseValue = baseValue + Math.random() * 20 - 10;
    for (let j = 0; j < 4; j++) {
      boxVals[j] = (Math.random() - 0.5) * dayRange + baseValue;
    }
    boxVals.sort();
    let openIdx = Math.round(Math.random() * 3);
    let closeIdx = Math.round(Math.random() * 2);
    if (closeIdx === openIdx) {
      closeIdx++;
    }
    let volumn = boxVals[3] * (1000 + Math.random() * 500);
    // ['open', 'close', 'lowest', 'highest', 'volumn']
    // [1, 4, 3, 2]
    data[i] = [
      echarts.format.formatTime('yyyy-MM-dd\nhh:mm:ss', (xValue += minute)),
      +boxVals[openIdx].toFixed(2),
      +boxVals[3].toFixed(2),
      +boxVals[0].toFixed(2),
      +boxVals[closeIdx].toFixed(2),
      +volumn.toFixed(0),
      getSign(data, i, +boxVals[openIdx], +boxVals[closeIdx], 4) // sign
    ];
  }
  return data;
  function getSign(data, dataIndex, openVal, closeVal, closeDimIdx) {
    var sign;
    if (openVal > closeVal) {
      sign = -1;
    } else if (openVal < closeVal) {
      sign = 1;
    } else {
      sign =
        dataIndex > 0
          ? // If close === open, compare with close of last record
            data[dataIndex - 1][closeDimIdx] <= closeVal
            ? 1
            : -1
          : // No record of previous, set to be positive
            1;
    }
    return sign;
  }
}
```

