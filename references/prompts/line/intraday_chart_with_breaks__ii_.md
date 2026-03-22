## 图表类型：断轴上的日内走势图 (II) (Intraday Chart with Breaks (II))

**生成指令**：你现在的任务是生成一个 ECharts 的 `option` 配置。请根据以下骨架代码和数据结构要求，结合用户的实际数据进行填充和修改，生成一份完整的图表配置参数。

### ECharts Option 骨架参考
请基于此结构（已剥离冗长写死的数据）生成配置。不要直接输出此骨架，而是要输出**包含真实数据和完整逻辑**的完整 `option` 对象：

```javascript
var formatTime = echarts.time.format;
var _data = generateData1();
option = {
  // Choose axis ticks based on UTC time.
  useUTC: true,
  title: {
    text: 'Intraday Chart with Breaks (Single Day)',
    left: 'center'
  },
  tooltip: {
    show: true,
    trigger: 'axis'
  },
  xAxis: [
    {
      type: 'time',
      interval: 1000 * 60 * 30,
      axisLabel: {
        showMinLabel: true,
        showMaxLabel: true,
        formatter: (value, index, extra) => {
          if (!extra || !extra.break) {
            // The third parameter is `useUTC: true`.
            return formatTime(value, '{HH}:{mm}', true);
          }
          // Only render the label on break start, but not on break end.
          if (extra.break.type === 'start') {
            return (
              formatTime(extra.break.start, '{HH}:{mm}', true) +
              '/' +
              formatTime(extra.break.end, '{HH}:{mm}', true)
            );
          }
          return '';
        }
      },
      breakLabelLayout: {
        // Disable auto move of break labels if overlapping,
        // and use `axisLabel.formatter` to control the label display.
        moveOverlap: false
      },
      breaks: [
        {
          start: _data.breakStart,
          end: _data.breakEnd,
          gap: 0
        }
      ],
      breakArea: {
        expandOnClick: false,
        zigzagAmplitude: 0,
        zigzagZ: 200
      }
    }
  ],
  yAxis: {
    type: 'value',
    min: 'dataMin'
  },
  dataZoom: [
    {
      type: 'inside',
      xAxisIndex: 0
    },
    {
      type: 'slider',
      xAxisIndex: 0
    }
  ],
  series: [
    {
      type: 'line',
      symbolSize: 0,
      data: _data.seriesData
    }
  ]
};
/**
 * Generate random data, not relevant to echarts API.
 */
function generateData1() {
  var seriesData = [];
  var time = new Date('2024-04-09T09:30:00Z');
  var endTime = new Date('2024-04-09T15:00:00Z').getTime();
  var breakStart = new Date('2024-04-09T11:30:00Z').getTime();
  var breakEnd = new Date('2024-04-09T13:00:00Z').getTime();
  for (var val = 1669; time.getTime() <= endTime; ) {
    if (time.getTime() <= breakStart || time.getTime() >= breakEnd) {
      val =
        val +
        Math.floor((Math.random() - 0.5 * Math.sin(val / 1000)) * 20 * 100) /
          100;
      val = +val.toFixed(2);
      seriesData.push([time.getTime(), val]);
    }
    time.setMinutes(time.getMinutes() + 1);
  }
  return {
    seriesData: seriesData,
    breakStart: breakStart,
    breakEnd: breakEnd
  };
}
```

