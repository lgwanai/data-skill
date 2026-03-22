## 图表类型：自定义特效 (GEO SVG with Customized Effect)

**生成指令**：你现在的任务是生成一个 ECharts 的 `option` 配置。请根据以下骨架代码和数据结构要求，结合用户的实际数据进行填充和修改，生成一份完整的图表配置参数。

### 图片资源提示
该图表需要加载以下类型的图片资源：
https://echarts.apache.org/examples/data/asset/geo/Map_of_Iceland.svg
请在生成代码时保留图片 URL 参数位置，并在最终输出时明确提示用户提供相应的图片资源 URL。

### ECharts Option 骨架参考
请基于此结构（已剥离冗长写死的数据）生成配置。不要直接输出此骨架，而是要输出**包含真实数据和完整逻辑**的完整 `option` 对象：

```javascript
$.get(ROOT_PATH + '/data/asset/geo/Map_of_Iceland.svg', function (svg) {
  echarts.registerMap('iceland_svg', { svg: svg });
  option = {
    tooltip: {},
    geo: {
      tooltip: {
        show: true
      },
      map: 'iceland_svg',
      roam: true
    },
    series: {
      type: 'custom',
      coordinateSystem: 'geo',
      geoIndex: 0,
      zlevel: 1,
      data: [
        [488.2358421078053, 459.70913833075736, 100],
        [770.3415644319939, 757.9672194986475, 30],
        [1180.0329284196291, 743.6141808346214, 80],
        [894.03790632245, 1188.1985153835008, 61],
        [1372.98925630313, 477.3839988649537, 70],
        [1378.62251255796, 935.6708486282843, 81]
      ],
      renderItem(params, api) {
        const coord = api.coord([
          api.value(0, params.dataIndex),
          api.value(1, params.dataIndex)
        ]);
        const circles = [];
        for (let i = 0; i < 5; i++) {
          circles.push({
            type: 'circle',
            shape: {
              cx: 0,
              cy: 0,
              r: 30
            },
            style: {
              stroke: 'red',
              fill: 'none',
              lineWidth: 2
            },
            // Ripple animation
            keyframeAnimation: {
              duration: 4000,
              loop: true,
              delay: (-i / 4) * 4000,
              keyframes: [
                {
                  percent: 0,
                  scaleX: 0,
                  scaleY: 0,
                  style: {
                    opacity: 1
                  }
                },
                {
                  percent: 1,
                  scaleX: 1,
                  scaleY: 0.4,
                  style: {
                    opacity: 0
                  }
                }
              ]
            }
          });
        }
        return {
          type: 'group',
          x: coord[0],
          y: coord[1],
          children: [
            ...circles,
            {
              type: 'path',
              shape: {
                d: 'M16 0c-5.523 0-10 4.477-10 10 0 10 10 22 10 22s10-12 10-22c0-5.523-4.477-10-10-10zM16 16c-3.314 0-6-2.686-6-6s2.686-6 6-6 6 2.686 6 6-2.686 6-6 6z',
                x: -10,
                y: -35,
                width: 20,
                height: 40
              },
              style: {
                fill: 'red'
              },
              // Jump animation.
              keyframeAnimation: {
                duration: 1000,
                loop: true,
                delay: Math.random() * 1000,
                keyframes: [
                  {
                    y: -10,
                    percent: 0.5,
                    easing: 'cubicOut'
                  },
                  {
                    y: 0,
                    percent: 1,
                    easing: 'bounceOut'
                  }
                ]
              }
            }
          ]
        };
      }
    }
  };
  myChart.setOption(option);
});
```

