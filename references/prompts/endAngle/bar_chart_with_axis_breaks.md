## 图表类型：断轴上的柱状图 (Bar Chart with Axis Breaks)

**生成指令**：你现在的任务是生成一个 ECharts 的 `option` 配置。请根据以下骨架代码和数据结构要求，结合用户的实际数据进行填充和修改，生成一份完整的图表配置参数。

### ECharts Option 骨架参考
请基于此结构（已剥离冗长写死的数据）生成配置。不要直接输出此骨架，而是要输出**包含真实数据和完整逻辑**的完整 `option` 对象：

```javascript
var _currentAxisBreaks = [
  {
    start: 5000,
    end: 100000,
    gap: '1.5%'
  },
  {
    // `start` and `end` are also used as the identifier for a certain axis break.
    start: 105000,
    end: 3100000,
    gap: '1.5%'
  }
];
option = {
  title: {
    text: 'Bar Chart with Axis Breaks',
    subtext: 'Click the break area to expand it',
    left: 'center',
    textStyle: {
      fontSize: 20
    },
    subtextStyle: {
      color: '#175ce5',
      fontSize: 15,
      fontWeight: 'bold'
    }
  },
  tooltip: {
    trigger: 'axis',
    axisPointer: {
      type: 'shadow'
    }
  },
  legend: {},
  grid: {
    top: 120
  },
  xAxis: [
    {
      type: 'category',
      data: [ /* 请使用用户的真实数据数组替换此处 */ ]
    }
  ],
  yAxis: [
    {
      type: 'value',
      breaks: _currentAxisBreaks,
      breakArea: {
        itemStyle: {
          opacity: 1
        },
        zigzagZ: 200
      }
    }
  ],
  series: [
    {
      name: 'Data A',
      type: 'bar',
      emphasis: {
        focus: 'series'
      },
      data: [ /* 请使用用户的真实数据数组替换此处 */ ]
    },
    {
      name: 'Data B',
      type: 'bar',
      emphasis: {
        focus: 'series'
      },
      data: [ /* 请使用用户的真实数据数组替换此处 */ ]
    },
    {
      name: 'Data C',
      type: 'bar',
      emphasis: {
        focus: 'series'
      },
      data: [ /* 请使用用户的真实数据数组替换此处 */ ]
    },
    {
      name: 'Data D',
      type: 'bar',
      data: [ /* 请使用用户的真实数据数组替换此处 */ ],
      emphasis: {
        focus: 'series'
      }
    }
  ]
};
/**
 * This is some interaction logic with axis break:
 *  - Click to expand and reset button.
 *
 * You can ignore this part if you do not need it.
 */
function initAxisBreakInteraction() {
  myChart.on('axisbreakchanged', function (params) {
    updateCollapseButton(params);
  });
  myChart.on('click', function (params) {
    if (params.name === 'collapseAxisBreakBtn') {
      collapseAxisBreak();
    }
  });
  function updateCollapseButton(params) {
    // If there is any axis break expanded, we need to show the collapse button.
    var needReset = false;
    for (let i = 0; i < params.breaks.length; i++) {
      const changedBreakItem = params.breaks[i];
      if (changedBreakItem.isExpanded) {
        needReset = true;
        break;
      }
    }
    myChart.setOption({
      // Draw the collapse button.
      graphic: [
        {
          elements: [
            {
              type: 'rect',
              ignore: !needReset,
              name: 'collapseAxisBreakBtn',
              top: 5,
              left: 5,
              shape: { r: 3, width: 140, height: 24 },
              style: { fill: '#eee', stroke: '#999', lineWidth: 1 },
              textContent: {
                type: 'text',
                style: {
                  text: 'Collapse Axis Breaks',
                  fontSize: 13,
                  fontWeight: 'bold'
                }
              },
              textConfig: { position: 'inside' }
            }
          ]
        }
      ]
    });
  }
  function collapseAxisBreak() {
    myChart.dispatchAction({
      type: 'collapseAxisBreak',
      yAxisIndex: 0,
      breaks: _currentAxisBreaks
    });
  }
} // End of initAxisBreakInteraction
setTimeout(initAxisBreakInteraction, 0);
```

