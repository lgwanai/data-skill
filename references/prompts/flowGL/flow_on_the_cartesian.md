## 图表类型：直角坐标系上的向量场 (Flow on the cartesian)

**生成指令**：你现在的任务是生成一个 ECharts 的 `option` 配置。请根据以下骨架代码和数据结构要求，结合用户的实际数据进行填充和修改，生成一份完整的图表配置参数。

### ECharts Option 骨架参考
请基于此结构（已剥离冗长写死的数据）生成配置。不要直接输出此骨架，而是要输出**包含真实数据和完整逻辑**的完整 `option` 对象：

```javascript
$.getScript(CDN_PATH + 'simplex-noise@2.4.0/simplex-noise.js').done(
  function () {
    var noise = new SimplexNoise(Math.random);
    var noise2 = new SimplexNoise(Math.random);
    function generateData() {
      var data = [];
      for (var i = 0; i <= 50; i++) {
        for (var j = 0; j <= 50; j++) {
          var dx = noise.noise2D(i / 30, j / 30);
          var dy = noise2.noise2D(i / 30, j / 30);
          var mag = Math.sqrt(dx * dx + dy * dy);
          valMax = Math.max(valMax, mag);
          valMin = Math.min(valMin, mag);
          data.push([i, j, dx, dy, mag]);
        }
      }
      return data;
    }
    var valMin = Infinity;
    var valMax = -Infinity;
    var data = generateData();
    myChart.setOption({
      visualMap: {
        show: false,
        min: valMin,
        max: valMax,
        dimension: 4,
        inRange: {
          color: [ /* 请使用用户的真实数据数组替换此处 */ ]
        }
      },
      xAxis: {
        type: 'value',
        axisLine: {
          lineStyle: {
            color: '#fff'
          }
        },
        splitLine: {
          show: false,
          lineStyle: {
            color: 'rgba(255,255,255,0.2)'
          }
        }
      },
      yAxis: {
        type: 'value',
        axisLine: {
          lineStyle: {
            color: '#fff'
          }
        },
        splitLine: {
          show: false,
          lineStyle: {
            color: 'rgba(255,255,255,0.2)'
          }
        }
      },
      series: [
        {
          type: 'flowGL',
          data: data,
          particleDensity: 64,
          particleSize: 5,
          itemStyle: {
            opacity: 0.5
          }
        },
        {
          type: 'custom',
          data: data,
          encode: {
            x: 0,
            y: 0
          },
          renderItem: function (params, api) {
            var x = api.value(0),
              y = api.value(1),
              dx = api.value(2),
              dy = api.value(3);
            var start = api.coord([x - dx / 2, y - dy / 2]);
            var end = api.coord([x + dx / 2, y + dy / 2]);
            return {
              type: 'line',
              shape: {
                x1: start[0],
                y1: start[1],
                x2: end[0],
                y2: end[1]
              },
              style: {
                lineWidth: 2,
                stroke: '#fff',
                opacity: 0.2
              }
            };
          }
        }
      ]
    });
  }
);
```

