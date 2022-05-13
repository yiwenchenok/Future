var get_bar_option = function (name, x_name, data_x, data_y) {
    return {
        title: {
            text: name,
        },
        tooltip: {
            trigger: 'axis'
        },
        legend: {
            data: [x_name,]
        },
        toolbox: {
            show: true,
            feature: {
                mark: {show: true},
                dataView: {show: true, readOnly: false},
                magicType: {show: true, type: ['line', 'bar']},
                restore: {show: true},
                saveAsImage: {show: true}
            }
        },
        calculable: true,
        xAxis: [
            {
                type: 'category',
                data: data_x,
                gridIndex: 0,
                axisLabel: {
                    // show: true,
                    interval: 0,
                    fontSize: 8,
                    rotate: 45
                },
            },
        ],
        yAxis: [
            {
                type: 'value'
            }
        ],
        series: [
            {
                name: x_name,
                type: 'bar',
                data: data_y,
                markPoint: {
                    data: [
                        {type: 'max', name: '最大值'},
                        {type: 'min', name: '最小值'}
                    ]
                },
                markLine: {
                    data: [
                        {type: 'average', name: '平均值'}
                    ]
                }
            }
        ]
    };
}

$(function () {
    $.get("/json_data/",
        function (data, status) {
            // 销量与价格的关系
            var my_char1 = echarts.init(document.getElementById("chart1"));
            var my_char2 = echarts.init(document.getElementById("chart2"));
            var my_char3 = echarts.init(document.getElementById("chart3"));
            // var my_char3 = echarts.init(document.querySelector(".line3 .chart"));
            // var my_char4 = echarts.init(document.querySelector(".line4 .chart"));
            // var my_char5 = echarts.init(document.querySelector(".line5 .chart"));
            var char1 = data['top_companyind']
            var companyind_list = char1[0]
            var companyind_count_list = char1[1]
            var option1 = get_bar_option('热门行业的用人需求Top10', '岗位数量', companyind_list, companyind_count_list)
            my_char1.setOption(option1);

            var char2 = data['top_city']
            var city_list = char2[0]
            var city_count_list = char2[1]
            var option2 = get_bar_option('热门城市的岗位数量Top10', '岗位数量', city_list, city_count_list)
            my_char2.setOption(option2);


            var city_pie = data['city_pie']
            var city = data['city']
            var option3 = option = {
                title: {
                    text: '一线城市岗位对比',
                    x: 'center'
                },
                tooltip: {
                    trigger: 'item',
                    formatter: "{a} <br/>{b} : {c} ({d}%)"
                },
                legend: {
                    orient: 'vertical',
                    x: 'left',
                    data: city
                },
                toolbox: {
                    show: true,
                    feature: {
                        mark: {show: true},
                        dataView: {show: true, readOnly: false},
                        magicType: {
                            show: true,
                            type: ['pie', 'funnel'],
                            option: {
                                funnel: {
                                    x: '25%',
                                    width: '50%',
                                    funnelAlign: 'left',
                                    max: 1548
                                }
                            }
                        },
                        restore: {show: true},
                        saveAsImage: {show: true}
                    }
                },
                calculable: true,
                series: [
                    {
                        name: '访问来源',
                        type: 'pie',
                        radius: '55%',
                        center: ['50%', '60%'],
                        data: city_pie
                    }
                ]
            };
            my_char3.setOption(option3)

            var my_char_map = echarts.init(document.getElementById("chart-map"));
            echarts.registerMap('china', geoJson);
            my_char_map.hideLoading();
            var geoCoordMap = {
                '台湾': [121.5135, 25.0308],
                '黑龙江': [127.9688, 45.368],
                '内蒙古': [110.3467, 41.4899],
                "吉林": [125.8154, 44.2584],
                '北京': [116.4551, 40.2539],
                "辽宁": [123.1238, 42.1216],
                "河北": [114.4995, 38.1006],
                "天津": [117.4219, 39.4189],
                "山西": [112.3352, 37.9413],
                "陕西": [109.1162, 34.2004],
                "甘肃": [103.5901, 36.3043],
                "宁夏": [106.3586, 38.1775],
                "青海": [101.4038, 36.8207],
                "新疆": [87.9236, 43.5883],
                "西藏": [91.11, 29.97],
                "四川": [103.9526, 30.7617],
                "重庆": [108.384366, 30.439702],
                "山东": [117.1582, 36.8701],
                "河南": [113.4668, 34.6234],
                "江苏": [118.8062, 31.9208],
                "安徽": [117.29, 32.0581],
                "湖北": [114.3896, 30.6628],
                "浙江": [119.5313, 29.8773],
                "福建": [119.4543, 25.9222],
                "江西": [116.0046, 28.6633],
                "湖南": [113.0823, 28.2568],
                "贵州": [106.6992, 26.7682],
                "云南": [102.9199, 25.4663],
                "广东": [113.12244, 23.009505],
                "广西": [108.479, 23.1152],
                "海南": [110.3893, 19.8516],
                '上海': [121.4648, 31.2891],

            };
            var province_data = data['province_data']
            var max = 480, min = 9; // todo
            var maxSize4Pin = 100, minSize4Pin = 20;
            var convertData = function (data) {
                var res = [];
                for (var i = 0; i < data.length; i++) {
                    var geoCoord = geoCoordMap[data[i].name];
                    if (geoCoord) {
                        res.push({
                            name: data[i].name,
                            value: geoCoord.concat(data[i].value)
                        });
                    }
                }
                return res;
            };
            var option_map = {
                backgroundColor: {
                    type: 'linear',
                    x: 0,
                    y: 0,
                    x2: 1,
                    y2: 1,
                    colorStops: [{
                        offset: 0, color: '#0f378f' // 0% 处的颜色
                    }, {
                        offset: 1, color: '#00091a' // 100% 处的颜色
                    }],
                    globalCoord: false // 缺省为 false
                },
                title: {
                    top: 20,
                    text: '全国各省岗位数量',
                    subtext: '',
                    x: 'center',
                    textStyle: {
                        color: '#ccc'
                    }
                },
                toolbox: {
                    show: true,
                    feature: {
                        restore: {show: true},
                        saveAsImage: {show: true}
                    }
                },

                tooltip: {
                    trigger: 'item',
                    formatter: function (params) {
                        if (typeof (params.value)[2] == "undefined") {
                            return params.name + ' : ' + params.value;
                        } else {
                            return params.name + ' : ' + params.value[2];
                        }
                    }
                },
                legend: {
                    orient: 'vertical',
                    y: 'bottom',
                    x: 'right',
                    data: ['岗位数量'],
                    textStyle: {
                        color: '#fff'
                    }
                },
                visualMap: {
                    show: false,
                    min: 0,
                    max: 500,
                    left: 'left',
                    top: 'bottom',
                    // text: ['高', '低'], // 文本，默认为数值文本
                    calculable: true,
                    seriesIndex: [1],
                    inRange: {}
                },
                geo: {
                    map: 'china',
                    show: true,
                    roam: true,
                    label: {
                        normal: {
                            show: false
                        },
                        emphasis: {
                            show: false,
                        }
                    },
                    itemStyle: {
                        normal: {
                            areaColor: '#3a7fd5',
                            borderColor: '#0a53e9',//线
                            shadowColor: '#092f8f',//外发光
                            shadowBlur: 20
                        },
                        emphasis: {
                            areaColor: '#0a2dae',//悬浮区背景
                        }
                    }
                },
                series: [
                    {

                        symbolSize: 5,
                        label: {
                            normal: {
                                formatter: '{b}',
                                position: 'right',
                                show: true
                            },
                            emphasis: {
                                show: true
                            }
                        },
                        itemStyle: {
                            normal: {
                                color: '#fff'
                            }
                        },
                        name: 'light',
                        type: 'scatter',
                        coordinateSystem: 'geo',
                        data: convertData(province_data),

                    },
                    {
                        type: 'map',
                        map: 'china',
                        geoIndex: 0,
                        aspectScale: 0.75, //长宽比
                        showLegendSymbol: false, // 存在legend时显示
                        label: {
                            normal: {
                                show: false
                            },
                            emphasis: {
                                show: false,
                                textStyle: {
                                    color: '#fff'
                                }
                            }
                        },
                        roam: true,
                        itemStyle: {
                            normal: {
                                areaColor: '#031525',
                                borderColor: '#FFFFFF',
                            },
                            emphasis: {
                                areaColor: '#2B91B7'
                            }
                        },
                        animation: false,
                        data: province_data
                    },
                    {
                        name: 'Top 5',
                        type: 'scatter',
                        coordinateSystem: 'geo',
                        symbol: 'pin',
                        symbolSize: [50, 50],
                        label: {
                            normal: {
                                show: true,
                                textStyle: {
                                    color: '#131212',
                                    fontSize: 10,
                                },
                                formatter(value) {
                                    return value.data.value[2]
                                }
                            }
                        },
                        itemStyle: {
                            normal: {
                                color: '#D8BC37', //标志颜色
                            }
                        },
                        data: convertData(province_data),
                        showEffectOn: 'render',
                        rippleEffect: {
                            brushType: 'stroke'
                        },
                        hoverAnimation: true,
                        zlevel: 1
                    },

                ]
            };
            my_char_map.setOption(option_map);

        })
})