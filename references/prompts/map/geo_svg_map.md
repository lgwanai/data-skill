## 图表类型：地图（SVG） (GEO SVG Map)

**生成指令**：你现在的任务是生成一个 ECharts 的 `option` 配置。请根据以下骨架代码和数据结构要求，结合用户的实际数据进行填充和修改，生成一份完整的图表配置参数。

### 图片资源提示
该图表需要加载以下类型的图片资源：
https://echarts.apache.org/examples/data/asset/geo/Sicily_prehellenic_topographic_map.svg
请在生成代码时保留图片 URL 参数位置，并在最终输出时明确提示用户提供相应的图片资源 URL。

### ECharts Option 骨架参考
请基于此结构（已剥离冗长写死的数据）生成配置。不要直接输出此骨架，而是要输出**包含真实数据和完整逻辑**的完整 `option` 对象：

```javascript
$.get(
  ROOT_PATH + '/data/asset/geo/Sicily_prehellenic_topographic_map.svg',
  function (svg) {
    echarts.registerMap('sicily', { svg: svg });
    option = {
      tooltip: {
        formatter: function (params) {
          console.log(params);
          return [
            params.name + ':',
            'xxxxxxxxxxxxxxxx',
            'xxxxxxxxxxxxxxxx',
            'xxxxxxxxxxxxxxxx'
          ].join('<br>');
        }
      },
      geo: [
        {
          map: 'sicily',
          roam: true,
          layoutCenter: ['50%', '50%'],
          layoutSize: '100%',
          selectedMode: 'single',
          tooltip: {
            show: true,
            confine: true,
            formatter: function (params) {
              return [ /* 请使用用户的真实数据数组替换此处 */ ].join('<br>');
            }
          },
          itemStyle: {
            color: undefined
          },
          emphasis: {
            label: {
              show: false
            }
          },
          select: {
            itemStyle: {
              color: '#b50205'
            },
            label: {
              show: false
            }
          },
          regions: [
            {
              name: 'route1',
              itemStyle: {
                borderWidth: 0
              },
              select: {
                itemStyle: {
                  color: '#b5280d',
                  borderWidth: 0
                }
              },
              tooltip: {
                position: 'right',
                alwaysShowContent: true,
                enterable: true,
                extraCssText: 'user-select: text',
                formatter: [ /* 请使用用户的真实数据数组替换此处 */ ].join('<br>')
              }
            },
            {
              name: 'route2',
              itemStyle: {
                borderWidth: 0
              },
              select: {
                itemStyle: {
                  color: '#b5280d',
                  borderWidth: 0
                }
              },
              tooltip: {
                position: 'left',
                alwaysShowContent: true,
                enterable: true,
                extraCssText: 'user-select: text',
                formatter: [ /* 请使用用户的真实数据数组替换此处 */ ].join('<br>')
              }
            }
          ]
        }
      ],
      // -------------
      // Make buttons
      grid: {
        top: 10,
        left: 'center',
        width: 80,
        height: 20
      },
      xAxis: {
        axisLine: { show: false },
        splitLine: { show: false },
        axisLabel: { show: false },
        axisTick: { show: false }
      },
      yAxis: {
        axisLine: { show: false },
        splitLine: { show: false },
        axisLabel: { show: false },
        axisTick: { show: false }
      },
      series: {
        type: 'scatter',
        itemStyle: {},
        label: {
          show: true,
          borderColor: '#999',
          borderWidth: 1,
          borderRadius: 2,
          backgroundColor: '#fff',
          padding: [3, 5],
          fontSize: 18,
          opacity: 1,
          color: '#333'
        },
        encode: {
          label: 2
        },
        symbolSize: 0,
        tooltip: { show: false },
        selectedMode: 'single',
        select: {
          label: {
            color: '#fff',
            borderColor: '#555',
            backgroundColor: '#555'
          }
        },
        data: [
          [0, 0, 'route1'],
          [1, 0, 'route2']
        ]
      }
      // Make buttons end
      // -----------------
    };
    myChart.setOption(option);
    myChart.on('selectchanged', function (params) {
      if (!params.selected.length) {
        myChart.dispatchAction({
          type: 'hideTip'
        });
        myChart.dispatchAction({
          type: 'geoSelect',
          geoIndex: 0
          // Use no name to unselect.
        });
      } else {
        var btnDataIdx = params.selected[0].dataIndex[0];
        var name = option.series.data[btnDataIdx][2];
        myChart.dispatchAction({
          type: 'geoSelect',
          geoIndex: 0,
          name: name
        });
        myChart.dispatchAction({
          type: 'showTip',
          geoIndex: 0,
          name: name
        });
      }
    });
  }
);
```

