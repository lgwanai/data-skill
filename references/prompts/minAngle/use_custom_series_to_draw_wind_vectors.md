## 图表类型：使用自定义系列绘制风场 (Use custom series to draw wind vectors)

**生成指令**：你现在的任务是生成一个 ECharts 的 `option` 配置。请根据以下骨架代码和数据结构要求，结合用户的实际数据进行填充和修改，生成一份完整的图表配置参数。

### 外部数据结构分析
该图表需要特定的外部数据结构支撑。以下是下载后的数据结构示例，请将用户的真实数据映射为类似结构：

**数据文件 [/data-gl/asset/data/winds.json]**:
```json
数据是一个对象 (Object)。包含的顶层字段示例：nx, ny, max, data。数据截取示例：
{
  "nx": 360,
  "ny": 181,
  "max": 28.700000762939453,
  "data": [
    [
      -2.9,
      4.2
    ],
    [
      -3,
      4.1
    ],
    [
      -3,
      4.1
    ],
    [
      -3.1,
      4
    ],
    [
      -3.2,
      4
    ],
    [
      -3.2,
      3.9
    ],
    [
      -3.3,
      3.9
    ],
    [
      -3.4,
      3.8
    ],
    [
      -3.4,
      3.8
    ],
    [
      -3.5,
      3.7
    ],
    [
      -3.6,
      3.6
    ],
    [
      -3.6,
      3.6
    ],
    [
      -3.7,
 ...
```

### ECharts Option 骨架参考
请基于此结构（已剥离冗长写死的数据）生成配置。不要直接输出此骨架，而是要输出**包含真实数据和完整逻辑**的完整 `option` 对象：

```javascript
function shuffle(array) {
  // https://stackoverflow.com/questions/2450954/how-to-randomize-shuffle-a-javascript-array
  var currentIndex = array.length;
  var temporaryValue;
  var randomIndex;
  // While there remain elements to shuffle...
  while (0 !== currentIndex) {
    // Pick a remaining element...
    randomIndex = Math.floor(Math.random() * currentIndex);
    currentIndex -= 1;
    // And swap it with the current element.
    temporaryValue = array[currentIndex];
    array[currentIndex] = array[randomIndex];
    array[randomIndex] = temporaryValue;
  }
  return array;
}
$.getJSON(ROOT_PATH + '/data-gl/asset/data/winds.json', function (windData) {
  var p = 0;
  var maxMag = 0;
  var minMag = Infinity;
  var data = [];
  for (var j = 0; j < windData.ny; j++) {
    for (var i = 0; i < windData.nx; i++, p++) {
      var vx = windData.data[p][0];
      var vy = windData.data[p][1];
      var mag = Math.sqrt(vx * vx + vy * vy);
      // 数据是一个一维数组
      // [ [经度, 维度，向量经度方向的值，向量维度方向的值] ]
      data.push([
        (i / windData.nx) * 360 - 180,
        (j / windData.ny) * 180 - 90,
        vx,
        vy,
        mag
      ]);
      maxMag = Math.max(mag, maxMag);
      minMag = Math.min(mag, minMag);
    }
  }
  shuffle(data);
  myChart.setOption(
    (option = {
      backgroundColor: '#333',
      visualMap: {
        left: 'center',
        min: minMag,
        max: maxMag,
        dimension: 4,
        inRange: {
          // prettier-ignore
          color: [ /* 请使用用户的真实数据数组替换此处 */ ]
        },
        calculable: true,
        textStyle: {
          color: '#fff'
        },
        orient: 'horizontal'
      },
      geo: {
        map: 'world',
        left: 0,
        right: 0,
        top: 0,
        zoom: 1,
        silent: true,
        roam: true,
        itemStyle: {
          areaColor: '#323c48',
          borderColor: '#111'
        }
      },
      series: {
        type: 'custom',
        coordinateSystem: 'geo',
        data: data,
        encode: {
          x: 0,
          y: 0
        },
        renderItem: function (params, api) {
          const x = api.value(0);
          const y = api.value(1);
          const dx = api.value(2);
          const dy = api.value(3);
          const start = api.coord([
            Math.max(x - dx / 5, -180),
            Math.max(y - dy / 5, -90)
          ]);
          const end = api.coord([
            Math.min(x + dx / 5, 180),
            Math.min(y + dy / 5, 90)
          ]);
          return {
            type: 'line',
            shape: {
              x1: start[0],
              y1: start[1],
              x2: end[0],
              y2: end[1]
            },
            style: {
              lineWidth: 0.5,
              stroke: api.visual('color')
            }
          };
        },
        progressive: 2000
      }
    })
  );
});
```

