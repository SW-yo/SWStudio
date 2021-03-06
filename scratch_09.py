import math, random, csv
import matplotlib.pyplot as plt
from collections import  Counter, defaultdict
import scratch_05 as sc5
from linear_algebra import shape, get_row, get_column, make_matrix, vector_mean, vector_sum, dot, magnitude, vector_subtract, scalar_multiply
from stats import correlation, standard_deviation, mean
import dateutil.parser


def bucketsize(point, bucket_size):
    #poitの値を切り捨てて場鉄の下限の値に備える
    return bucket_size * math.floor(point / bucket_size)

def make_histgram(points, bucket_size):
    #pointをバケツに入れ、何個入ったか数える
    return Counter(bucketsize(point, bucket_size) for point in points)

def plot_histgramu(points, bucket_size, title=""):
    histgram = make_histgram(points, bucket_size)
    plt.bar(histgram.keys(), histgram.values(), width=bucket_size)
    plt.title(title)
    plt.show()

random.seed(0)

#-100から100までの一様分布
uniform = [200 * random.random() - 100 for _ in range(10000)]

#平均0，標準偏差57の正規分布
normal = [57 * sc5.inverse_normal_cdf(random.random()) for _ in range(10000)]


#plot_histgramu(uniform, 10, "Uniform Histgram")
#plot_histgramu(normal, 10, "Normal Histgram")

def random_normal():
    #標準正規分布に従う無作為の数を返す
    return sc5.inverse_normal_cdf(random.random())


xs = [random_normal() for _ in range(1000)]
ys1 = [x + random_normal() / 2 for x in xs]
ys2 = [-x + random_normal() / 2 for x in xs]
"""
plt.scatter(xs, ys1, marker='.', color='black', label='y1')
plt.scatter(xs, ys2, marker='.', color='grey', label='ys2')
plt.xlabel('xs')
plt.ylabel('ys')
plt.legend(loc=9)
plt.title("Very Differnt Joint Distributions")
plt.show()
"""

num_points = 100

def random_row():
        row = [None, None, None, None]
        row[0] = random_normal()
        row[1] = -5 * row[0] + random_normal()
        row[2] = row[0] + row[1] + 5 * random_normal()
        row[3] = 6 if row[2] > -2 else 0
        return row
random.seed(0)
data = [random_row() for _ in range(num_points)]



def correlation_matrix(data):
    #i列とj列のデータ間の相関を(i, j)の値とすると、列数×列数の行列を返す

    _, num_colums = shape(data)

    def matrix_entry(i, j):
        return correlation(get_column(data, i), get_column(data, j))

    return make_matrix(num_colums, num_colums, matrix_entry)


_, num_colums = shape(data)
fig, ax = plt.subplots(num_colums, num_colums)

for i in range(num_colums):
    for j in range(num_colums):

        #X軸のcolumns_j、Y軸のcolumns_iの位置に散布図を描画する
        if i != j: ax[i][j].scatter(get_column(data, j), get_column(data, i))

        #i == jであれば列名を表示する
        else: ax[i][j].annotate("series " + str(i), (0.5, 0.5),
                                xycoords='axes fraction',
                                ha="center", va='center')

        #左端と一番下のサブプロット以外は軸ラベルを表示しない
        if i < num_colums - 1: ax[i][j].xaxis.set_visible(False)
        if j > 0: ax[i][j].yaxis.set_visible(False)

#右下と左上のサブプロットはテキストのみ表示しているため
#軸ラベルが誤っている
ax[-1][-1].set_xlim(ax[0][-1].get_xlim())
ax[0][0].set_ylim(ax[0][1].get_ylim())

#plt.show()

"""
def parse_row(input_row, pasers):
    #与えられたパーサのリスト（そのうちいくつかはNone)
    #の中から入力の列ごとに適切なものを適用する
     return [paser(value) if parser is not None else value
            for value, parser in zip(input_row, parsers)]

def parse_rows_with(reader, parsers):
    #readerをラップして入力の各列にパーサを適用する
    for row in reader:
        yield parse_row(row, parsers)

def try_or_none(f):
    #関数fが例外を起こした場合にはNoneを返す
    #fは1つだけの入力を想定する
    def f_or_none(x):
        try: return f(x)
        except: return None
    return f_or_none

def parse_row(input_row, parsers):
    return [try_or_none(parser)(value) if parser is not None else value
            for value, parser in zip(input_row,parsers)]


with open("comma_delimited_stock_prices.csv", "r") as f:
    reader = csv.reader(f)
    for line in parse_rows_with(reader, [dateutil.parser.parse, None, float]):
        data.append(line)

for row in data:
    if any(x is None for x in row):
        print(row)

def try_parse_field(field_name, value, parser_dict):
    #parser_dictの適切な関数を使って値を解釈する
    parser = parser_dict.get(field_name)            #対応する値がなければNoneが返る
    if parser is not None:
        return try_or_none(parser)(value)
    else:
        return value

def parse_dict(input_dict, parser_dict):
    return { field_name : try_parse_field(field_name, value, parser_dict)
            for field_name, value in  input_dict.items()}


def picker(field_name):
    #辞書から列を取り出す関数を返す
    return lambda row: row[field_name]

def pluck(field_name, rows):
    #辞書のリストから指定していした列のリストに変換する
    return map(picker(field_name), rows)

def group_by(grouper, rows, value_transform=None):
    #キーはグループ化関数の出力、値は行のリスト
    grouped = defaultdict(list)
    for row in rows:
        grouped[grouper(row)].append(row)

        if value_transform is None:
            return grouped
        else:
            return { key : value_transform(rows)
                    for key, rows in grouped.items()}

def percent_price_change(yesterday, today):
    return today["closing_price"] / yesterday["closing_price"] - 1

def day_over_dey_changes(grouped_rows):
    #行を日付でソートする
    ordered = sorted (grouped_rows, key=picker("date"))

    #連続した2日分のデータを組にするため、１つずらしたリストをzipする
    return [{ "symbol" : today["symbol"],
             "date" : today["date"],
             "change" : percent_price_change(yesterday, today)}
             for yesterday, today in zip(ordered, ordered[1:])]

#キーが銘柄（symbol)、値は前日比の辞書
change_by_symbol = group_by(picker("symbol"), data, day_over_dey_changes)

#すべての前日比の辞書を大きなリストに格納する
all_changes = [change
                for changes in changes_by_symbol.values()
                for change in changes]

"""

X = [
    [20.9666776351559,-13.1138080189357],
    [22.7719907680008,-19.8890894944696],
    [25.6687103160153,-11.9956004517219],
    [18.0019794950564,-18.1989191165133],
    [21.3967402102156,-10.8893126308196],
    [0.443696899177716,-19.7221132386308],
    [29.9198322142127,-14.0958668502427],
    [19.0805843080126,-13.7888747608312],
    [16.4685063521314,-11.2612927034291],
    [21.4597664701884,-12.4740034586705],
    [3.87655283720532,-17.575162461771],
    [34.5713920556787,-10.705185165378],
    [13.3732115747722,-16.7270274494424],
    [20.7281704141919,-8.81165591556553],
    [24.839851437942,-12.1240962157419],
    [20.3019544741252,-12.8725060780898],
    [21.9021426929599,-17.3225432396452],
    [23.2285885715486,-12.2676568419045],
    [28.5749111681851,-13.2616470619453],
    [29.2957424128701,-14.6299928678996],
    [15.2495527798625,-18.4649714274207],
    [26.5567257400476,-9.19794350561966],
    [30.1934232346361,-12.6272709845971],
    [36.8267446011057,-7.25409849336718],
    [32.157416823084,-10.4729534347553],
    [5.85964365291694,-22.6573731626132],
    [25.7426190674693,-14.8055803854566],
    [16.237602636139,-16.5920595763719],
    [14.7408608850568,-20.0537715298403],
    [6.85907008242544,-18.3965586884781],
    [26.5918329233128,-8.92664811750842],
    [-11.2216019958228,-27.0519081982856],
    [8.93593745011035,-20.8261235122575],
    [24.4481258671796,-18.0324012215159],
    [2.82048515404903,-22.4208457598703],
    [30.8803004755948,-11.455358009593],
    [15.4586738236098,-11.1242825084309],
    [28.5332537090494,-14.7898744423126],
    [40.4830293441052,-2.41946428697183],
    [15.7563759125684,-13.5771266003795],
    [19.3635588851727,-20.6224770470434],
    [13.4212840786467,-19.0238227375766],
    [7.77570680426702,-16.6385739839089],
    [21.4865983854408,-15.290799330002],
    [12.6392705930724,-23.6433305964301],
    [12.4746151388128,-17.9720169566614],
    [23.4572410437998,-14.602080545086],
    [13.6878189833565,-18.9687408182414],
    [15.4077465943441,-14.5352487124086],
    [20.3356581548895,-10.0883159703702],
    [20.7093833689359,-12.6939091236766],
    [11.1032293684441,-14.1383848928755],
    [17.5048321498308,-9.2338593361801],
    [16.3303688220188,-15.1054735529158],
    [26.6929062710726,-13.306030567991],
    [34.4985678099711,-9.86199941278607],
    [39.1374291499406,-10.5621430853401],
    [21.9088956482146,-9.95198845621849],
    [22.2367457578087,-17.2200123442707],
    [10.0032784145577,-19.3557700653426],
    [14.045833906665,-15.871937521131],
    [15.5640911917607,-18.3396956121887],
    [24.4771926581586,-14.8715313479137],
    [26.533415556629,-14.693883922494],
    [12.8722580202544,-21.2750596021509],
    [24.4768291376862,-15.9592080959207],
    [18.2230748567433,-14.6541444069985],
    [4.1902148367447,-20.6144032528762],
    [12.4332594022086,-16.6079789231489],
    [20.5483758651873,-18.8512560786321],
    [17.8180560451358,-12.5451990696752],
    [11.0071081078049,-20.3938092335862],
    [8.30560561422449,-22.9503944138682],
    [33.9857852657284,-4.8371294974382],
    [17.4376502239652,-14.5095976075022],
    [29.0379635148943,-14.8461553663227],
    [29.1344666599319,-7.70862921632672],
    [32.9730697624544,-15.5839178785654],
    [13.4211493998212,-20.150199857584],
    [11.380538260355,-12.8619410359766],
    [28.672631499186,-8.51866271785711],
    [16.4296061111902,-23.3326051279759],
    [25.7168371582585,-13.8899296143829],
    [13.3185154732595,-17.8959160024249],
    [3.60832478605376,-25.4023343597712],
    [39.5445949652652,-11.466377647931],
    [25.1693484426101,-12.2752652925707],
    [25.2884257196471,-7.06710309184533],
    [6.77665715793125,-22.3947299635571],
    [20.1844223778907,-16.0427471125407],
    [25.5506805272535,-9.33856532270204],
    [25.1495682602477,-7.17350567090738],
    [15.6978431006492,-17.5979197162642],
    [37.42780451491,-10.843637288504],
    [22.974620174842,-10.6171162611686],
    [34.6327117468934,-9.26182440487384],
    [34.7042513789061,-6.9630753351114],
    [15.6563953929008,-17.2196961218915],
    [25.2049825789225,-14.1592086208169]
]


def scale(data_matrix):
    #各列の平均と標準偏差を返す
    num_rows, num_cols = shape(data_matrix)
    means = [mean(get_column(data_matrix, j)) for j in range(num_cols)]
    stdevs = [standard_deviation(get_column(data_matrix, j)) for j in range(num_cols)]
    return means, stdevs

def rescale(data_matrix):
    #各列が平均0、標準偏差1となるように入力データのスケールを修正する
    #標準偏差が0の列は表示しない
    maens, stdevs = scal(data_matrix)

    def rescaled(i, j):
        if stdevs[j] > 0:
            return (data_matrix[i][j] - means[j]) / stdevs[j]
        else:
            return data_matrix[i][j]

    num_rows, num_colums = shape(data_matrix)
    return make_matrix(num_rows, num_colums, rescaled)

def de_mean_matrix(A):
    #Aのすべての値と各列の平均との差を返す。
    #結果の行列は各列の平均が0となる
    nr, nc = shape(A)
    column_means, _ = scale(A)
    return make_matrix(nr, nc, lambda i, j: A[i][j] - column_means[j])

def direction(w):
    mag = magnitude(w)
    return [w_i / mag for w_i in w]

def directional_variance_i(x_i, w):
    #wで示される方向に対する、x_iの分散を求める
    return dot(x_i, directon(w)) ** 2

def directional_variance(X, w):
    #wで示される方向に対する、データの分散を求める
    return sum(directional_variance_i(x_i, w) for x_i in X)

def directional_variance_gradient_i(x_i, w):
    #x_i列の値がw方向に持つ分散に対する購買
    projection_length = dot(x_i, direction(w))
    return [2 * projection_length * x_ij for x_ij in x_i]

def directional_variance_gradient(X, w):
    return vector_sum(directional_variance_gradient_i(x_i, w) for x_i in X)

def first_principal_component(X):
    guess = [1 for _ in X[0]]
    unscaled_maximizer = maxmize_batch(
        partial(directional_variance, X),           #これでwの関数となる
        partial(directional_variance_gradient, X),  #これでwの関数となる
        guess)
    return direction(unscaled_maximizer)

#ここでは"y"を使わないので、Noneのベクトルを渡す
#受け取る側の関数は、その入力を無視する
def first_principal_component_sgd(X):
    guess = [1 for _ in X[0]]
    unscaled_maximizer = maximize_stochastic(
        lambda x, _, w: directional_variance_i(x, w),
        lambda x, _, w: directional_variance_gradient_i(x, w),
        X,
        [None for _ in X],  #the fake "y"
        guess)
    return direction(unscaled_maximizer)

def project(v, w):
    #vをw方向に投影したベクトルを返す
    projection_length = dot(v, w)
    return scalar_multiply(projection_length, w)

def remove_projection_from_vector(v, w):
    #vをw方向へ射影した結果をvから取り除く
    return vector_subtract(v, project(v, w))

def remove_projection(X, w):
    #Xの各列に対して、w方向への射影結果を各列から取り除く
    return [remove_projection_from_vector(x_i, w) for x_i in X]

def principal_component_analysis(X, num_components):
    components = []
    for _ in range(num_components):
        component = first_principal_component(X)
        components.append(component)
        X = remove_projection(X, component)

    return components

def transform_vector(v, components):
    return [dot(v, w) for w in components]

def transform(X, components):
    return [transform_vector(x_i, components) for x_i in X]
