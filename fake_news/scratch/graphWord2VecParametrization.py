import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


windows = [1,2,3, 4, 6, 10, 20, 50, 100]
sizes = [10, 25, 50, 100, 300, 500, 750, 1000, 2000]
# word2vec = Word2VecSimple(min_count = 0, size = size, window = window, vectorization_function = "max") #vectorization_function maxmin, max, avg
raw_results = [[[0.5078864353312302, 0.5468053491827638, 0.6562847608453838, 0.5476190476190476, 0.5062893081761005, 0.5070866141732284, 0.5094339622641509, 0.6585365853658537, 0.5078864353312302, 0.6787620064034152], [0.6254295532646048, 0.6290598290598289, 0.6301369863013698, 0.6301369863013698, 0.6267123287671234, 0.6267123287671234, 0.62778730703259, 0.62778730703259, 0.6254295532646048, 0.6267123287671234], [0.49800796812749004, 0.503968253968254, 0.5049701789264414, 0.4970178926441352, 0.4970178926441352, 0.4970178926441352, 0.4990019960079841, 0.4970178926441352, 0.4990019960079841, 0.568904593639576], [0.5862068965517241, 0.5862068965517241, 0.5862068965517241, 0.5862068965517241, 0.5862068965517241, 0.5862068965517241, 0.5862068965517241, 0.5862068965517241, 0.5862068965517241, 0.5862068965517241], [0.6331658291457287, 0.6331658291457287, 0.6323713927227101, 0.6331658291457287, 0.6323713927227101, 0.6309226932668329, 0.6323713927227101, 0.6331658291457287, 0.6331658291457287, 0.6331658291457287], [0.6420664206642066, 0.6420664206642066, 0.6420664206642066, 0.6420664206642066, 0.6428571428571429, 0.6420664206642066, 0.6428571428571429, 0.6428571428571429, 0.6420664206642066, 0.6428571428571429], [0.632258064516129, 0.606951871657754, 0.628719275549806, 0.6304909560723515, 0.6045272969374168, 0.6077643908969209, 0.6269430051813472, 0.627906976744186, 0.6053333333333334, 0.6008010680907877], [0.6825053995680345, 0.6803455723542117, 0.6810344827586207, 0.681081081081081, 0.6803455723542117, 0.6803455723542117, 0.6817691477885652, 0.679611650485437, 0.6803455723542117, 0.6803455723542117], [0.6467661691542289, 0.6475716064757161, 0.6501240694789082, 0.6468401486988846, 0.6509316770186335, 0.6493184634448574, 0.6475716064757161, 0.6493184634448574, 0.6484472049689441, 0.6485148514851486]], [[0.22564102564102564, 0.2222222222222222, 0.22279792746113988, 0.2262210796915167, 0.22395833333333334, 0.22279792746113988, 0.22564102564102564, 0.2222222222222222, 0.22279792746113988, 0.22564102564102564], [0.6175942549371634, 0.6175942549371634, 0.6175942549371634, 0.6162162162162164, 0.6175942549371634, 0.6153846153846154, 0.6175942549371634, 0.6173285198555958, 0.6175942549371634, 0.6162162162162164], [0.6745718050065876, 0.6745718050065876, 0.6737120211360634, 0.6745718050065876, 0.6737120211360634, 0.6736842105263157, 0.6745718050065876, 0.6736842105263157, 0.6746031746031745, 0.6737120211360634], [0.676923076923077, 0.6784869976359339, 0.6784869976359339, 0.676923076923077, 0.6761565836298933, 0.6761565836298933, 0.6777251184834124, 0.676923076923077, 0.6777251184834124, 0.6784869976359339], [0.6821345707656613, 0.6806039488966318, 0.6873563218390805, 0.6881472957422325, 0.6873563218390805, 0.6858457997698505, 0.6858457997698505, 0.6829268292682926, 0.6866359447004609, 0.6836616454229432], [0.6777251184834124, 0.6800947867298579, 0.6785290628706999, 0.6761565836298933, 0.6800947867298579, 0.6777251184834124, 0.6785290628706999, 0.6792899408284023, 0.6800947867298579, 0.6785290628706999], [0.6788008565310492, 0.6788399570354458, 0.6802575107296137, 0.6788008565310492, 0.6773847802786709, 0.6773847802786709, 0.6788008565310492, 0.6773847802786709, 0.6773847802786709, 0.6802575107296137], [0.5515151515151514, 0.5537065052950076, 0.5537065052950076, 0.5515151515151514, 0.5515151515151514, 0.5515151515151514, 0.5537065052950076, 0.5515151515151514, 0.5515151515151514, 0.5515151515151514], [0.6882217090069284, 0.6867052023121388, 0.6867052023121388, 0.6882217090069284, 0.6882217090069284, 0.6882217090069284, 0.6867052023121388, 0.6882217090069284, 0.6867052023121388, 0.6882217090069284]], [[0.5345622119815668, 0.5345622119815668, 0.5345622119815668, 0.5345622119815668, 0.5345622119815668, 0.5337423312883437, 0.5345622119815668, 0.5345622119815668, 0.5345622119815668, 0.5345622119815668], [0.6964285714285715, 0.6941964285714286, 0.6972067039106146, 0.6957494407158837, 0.6948775055679288, 0.6972067039106146, 0.6941964285714286, 0.6957494407158837, 0.6972067039106146, 0.6957494407158837], [0.5904059040590407, 0.5884543761638734, 0.5904059040590407, 0.5904059040590407, 0.5904059040590407, 0.5862708719851576, 0.5884543761638734, 0.5904059040590407, 0.5904059040590407, 0.5904059040590407], [0.6402188782489739, 0.6431478968792401, 0.6421768707482992, 0.6402188782489739, 0.6402188782489739, 0.6420765027322404, 0.6413043478260869, 0.6413043478260869, 0.6420765027322404, 0.6429548563611491], [0.6403269754768393, 0.6420765027322404, 0.6403269754768393, 0.6403269754768393, 0.6403269754768393, 0.6403269754768393, 0.6403269754768393, 0.6403269754768393, 0.6420765027322404, 0.6403269754768393], [0.6915254237288136, 0.6915254237288136, 0.6878547105561861, 0.6915254237288136, 0.6923076923076923, 0.6915254237288136, 0.6997792494481236, 0.6915254237288136, 0.6878547105561861, 0.6900452488687783], [0.661558109833972, 0.661558109833972, 0.661558109833972, 0.661558109833972, 0.661558109833972, 0.661558109833972, 0.661558109833972, 0.661558109833972, 0.661558109833972, 0.661558109833972], [0.6607142857142857, 0.6607142857142857, 0.6624203821656051, 0.6607142857142857, 0.6607142857142857, 0.6607142857142857, 0.6607142857142857, 0.6607142857142857, 0.6607142857142857, 0.6607142857142857], [0.6872146118721462, 0.6887115165336374, 0.6872146118721462, 0.6872146118721462, 0.6887115165336374, 0.6872146118721462, 0.6864310148232612, 0.6872146118721462, 0.6872146118721462, 0.6872146118721462]], [[0.6775599128540305, 0.6795698924731183, 0.6775599128540305, 0.6775599128540305, 0.6775599128540305, 0.6775599128540305, 0.6768226332970619, 0.6768226332970619, 0.6768226332970619, 0.6775599128540305], [0.6695938529088913, 0.6695938529088913, 0.6695938529088913, 0.6695938529088913, 0.6695938529088913, 0.6695938529088913, 0.6695938529088913, 0.6695938529088913, 0.6695938529088913, 0.6695938529088913], [0.692488262910798, 0.6916764361078547, 0.6916764361078547, 0.692488262910798, 0.6916764361078547, 0.6916764361078547, 0.692488262910798, 0.692488262910798, 0.6916764361078547, 0.692488262910798], [0.6931155192532089, 0.6931155192532089, 0.6923076923076922, 0.6931155192532089, 0.6923076923076922, 0.6923076923076922, 0.6931155192532089, 0.6923076923076922, 0.6931155192532089, 0.6923076923076922], [0.6948356807511737, 0.6948356807511737, 0.694021101992966, 0.694021101992966, 0.6948356807511737, 0.6948356807511737, 0.6948356807511737, 0.6933019976498237, 0.6933019976498237, 0.692488262910798], [0.6494178525226391, 0.6494178525226391, 0.6494178525226391, 0.6494178525226391, 0.6494178525226391, 0.6494178525226391, 0.6485788113695089, 0.6494178525226391, 0.6477419354838709, 0.6494178525226391], [0.5430016863406408, 0.5430016863406408, 0.5430016863406408, 0.5430016863406408, 0.5451505016722408, 0.5430016863406408, 0.5451505016722408, 0.5451505016722408, 0.5430016863406408, 0.5451505016722408], [0.6960451977401131, 0.6960451977401131, 0.6960451977401131, 0.6960451977401131, 0.6960451977401131, 0.6960451977401131, 0.6960451977401131, 0.6960451977401131, 0.6960451977401131, 0.6960451977401131], [0.6960451977401131, 0.6938775510204082, 0.6938775510204082, 0.6938775510204082, 0.6960451977401131, 0.6960451977401131, 0.6952595936794582, 0.6938775510204082, 0.6938775510204082, 0.6938775510204082]], [[0.6666666666666667, 0.6666666666666667, 0.6666666666666667, 0.6658653846153846, 0.6666666666666667, 0.6666666666666667, 0.6666666666666667, 0.6658653846153846, 0.6658653846153846, 0.6666666666666667], [0.6577669902912622, 0.6577669902912622, 0.6553398058252428, 0.6561360874848117, 0.6577669902912622, 0.6561360874848117, 0.6577669902912622, 0.6553398058252428, 0.6561360874848117, 0.6577669902912622], [0.7037037037037036, 0.7037037037037036, 0.7037037037037036, 0.7037037037037036, 0.7037037037037036, 0.7037037037037036, 0.7037037037037036, 0.7037037037037036, 0.7037037037037036, 0.7037037037037036], [0.6370757180156659, 0.6388526727509779, 0.6370757180156659, 0.6370757180156659, 0.6370757180156659, 0.6388526727509779, 0.6370757180156659, 0.6370757180156659, 0.6370757180156659, 0.6370757180156659], [0.6816037735849056, 0.6816037735849056, 0.6737841043890866, 0.6816037735849056, 0.6816037735849056, 0.6737841043890866, 0.6737841043890866, 0.6816037735849056, 0.6737841043890866, 0.6816037735849056], [0.7025813692480359, 0.6996625421822272, 0.6996625421822272, 0.7003367003367003, 0.7003367003367003, 0.7003367003367003, 0.7004504504504505, 0.7003367003367003, 0.6996625421822272, 0.6996625421822272], [0.6792452830188679, 0.6761565836298933, 0.680047225501771, 0.6769596199524941, 0.6761565836298933, 0.6784452296819787, 0.6784452296819787, 0.6768867924528302, 0.6753554502369669, 0.6799531066822978], [0.6623711340206186, 0.6623711340206186, 0.6623711340206186, 0.6623711340206186, 0.6615186615186615, 0.6615186615186615, 0.6623711340206186, 0.6623711340206186, 0.6632390745501285, 0.6623711340206186], [0.6553966189856957, 0.6553966189856957, 0.6691823899371069, 0.6545454545454545, 0.657142857142857, 0.6553966189856957, 0.6580310880829016, 0.6649810366624526, 0.6580310880829016, 0.6580310880829016]], [[0.6837606837606837, 0.6844349680170576, 0.6844349680170576, 0.6825053995680345, 0.6837606837606837, 0.6839266450916937, 0.6844349680170576, 0.6837060702875399, 0.6865671641791046, 0.6837606837606837], [0.5577211394302848, 0.5585585585585585, 0.556390977443609, 0.5555555555555557, 0.5585585585585585, 0.556390977443609, 0.5585585585585585, 0.5577211394302848, 0.5555555555555557, 0.556390977443609], [0.6429548563611491, 0.6429548563611491, 0.6429548563611491, 0.6429548563611491, 0.6420765027322404, 0.6429548563611491, 0.6420765027322404, 0.6429548563611491, 0.6429548563611491, 0.6429548563611491], [0.6374829001367989, 0.6364883401920439, 0.641200545702592, 0.6374829001367989, 0.6383561643835616, 0.641200545702592, 0.6374829001367989, 0.641200545702592, 0.6374829001367989, 0.6374829001367989], [0.6485013623978201, 0.6504065040650405, 0.6494565217391304, 0.6457765667574932, 0.6512890094979648, 0.6504065040650405, 0.6467391304347826, 0.6504065040650405, 0.6467391304347826, 0.6512890094979648], [0.5714285714285715, 0.5710102489019033, 0.5722627737226278, 0.5730994152046784, 0.5714285714285715, 0.5743440233236152, 0.5701754385964912, 0.56973293768546, 0.5735080058224165, 0.5714285714285715], [0.576419213973799, 0.5800865800865801, 0.5755813953488372, 0.5755813953488372, 0.5751824817518248, 0.5743440233236152, 0.5743440233236152, 0.5776487663280117, 0.5780346820809248, 0.577259475218659], [0.6589446589446589, 0.6589446589446589, 0.6589446589446589, 0.6606683804627249, 0.6571798188874516, 0.6589446589446589, 0.655483870967742, 0.6589446589446589, 0.6589147286821705, 0.6606683804627249], [0.5701624815361891, 0.5701624815361891, 0.6910656620021529, 0.5701624815361891, 0.5701624815361891, 0.5701624815361891, 0.5710059171597633, 0.5701624815361891, 0.5701624815361891, 0.5701624815361891]], [[0.5648414985590778, 0.5751072961373391, 0.5730659025787965, 0.5669064748201439, 0.573466476462197, 0.5751072961373391, 0.5652797704447634, 0.5722460658082975, 0.5624103299856528, 0.5685714285714285], [0.6381842456608812, 0.6336898395721926, 0.6336898395721926, 0.6381842456608812, 0.6381842456608812, 0.6345381526104418, 0.6336898395721926, 0.6345381526104418, 0.6373333333333334, 0.6345381526104418], [0.6421768707482992, 0.6440217391304348, 0.6421768707482992, 0.645945945945946, 0.6441136671177267, 0.6441136671177267, 0.6421768707482992, 0.645945945945946, 0.6441136671177267, 0.645945945945946], [0.6927784577723378, 0.6928746928746929, 0.6936274509803921, 0.696078431372549, 0.6936274509803921, 0.6904176904176903, 0.6920245398773007, 0.6928746928746929, 0.6912669126691268, 0.6912669126691268], [0.6844783715012722, 0.6870229007633587, 0.6861499364675985, 0.6846153846153846, 0.6862244897959183, 0.6844783715012722, 0.6870229007633587, 0.6845466155810983, 0.6862244897959183, 0.6854219948849104], [0.703883495145631, 0.7047387606318348, 0.703883495145631, 0.703883495145631, 0.703883495145631, 0.703883495145631, 0.7047387606318348, 0.703883495145631, 0.703883495145631, 0.7047387606318348], [0.6580645161290323, 0.6633291614518146, 0.655483870967742, 0.6658291457286433, 0.6563307493540051, 0.6649937264742785, 0.6572164948453608, 0.654639175257732, 0.6572164948453608, 0.6563307493540051], [0.6580976863753213, 0.650259067357513, 0.6598726114649681, 0.6580976863753213, 0.6598726114649681, 0.6519480519480519, 0.6493506493506493, 0.6563706563706564, 0.6589446589446589, 0.6590038314176245], [0.5780346820809248, 0.5676077265973254, 0.5590433482810164, 0.5680473372781065, 0.5759768451519537, 0.5620328849028401, 0.5784883720930234, 0.5722627737226278, 0.5637982195845698, 0.5739385065885798]], [[0.5702005730659025, 0.5702005730659025, 0.5702005730659025, 0.5702005730659025, 0.5660919540229885, 0.5702005730659025, 0.5702005730659025, 0.5702005730659025, 0.5660919540229885, 0.5660919540229885], [0.6350974930362117, 0.6333333333333333, 0.639777468706537, 0.6359832635983264, 0.639777468706537, 0.6342141863699583, 0.638888888888889, 0.6384720327421555, 0.6371191135734071, 0.6342141863699583], [0.6408839779005525, 0.64, 0.639777468706537, 0.64, 0.64, 0.6407766990291263, 0.639777468706537, 0.6408839779005525, 0.64, 0.6408839779005525], [0.7028360049321825, 0.7019704433497537, 0.7044334975369458, 0.7019704433497537, 0.7019704433497537, 0.7019704433497537, 0.7061668681983072, 0.7028360049321825, 0.7019704433497537, 0.7028360049321825], [0.6956521739130435, 0.6956521739130435, 0.6956521739130435, 0.6956521739130435, 0.6956521739130435, 0.6931677018633541, 0.6956521739130435, 0.6923076923076923, 0.6923076923076923, 0.6940298507462687], [0.6538952745849297, 0.6547314578005115, 0.6529562982005142, 0.6555697823303457, 0.6538952745849297, 0.6556122448979592, 0.6537966537966537, 0.6556122448979592, 0.6564495530012772, 0.6538952745849297], [0.6675, 0.6563706563706564, 0.6580976863753213, 0.6563706563706564, 0.6563706563706564, 0.6563706563706564, 0.6563706563706564, 0.658974358974359, 0.6555269922879178, 0.6563706563706564], [0.6355140186915889, 0.6355140186915889, 0.631578947368421, 0.6307277628032345, 0.6324324324324324, 0.6324324324324324, 0.631578947368421, 0.6239782016348774, 0.6338215712383488, 0.6355140186915889], [0.6563706563706564, 0.6545924967658474, 0.6545924967658474, 0.6493506493506493, 0.6572528883183569, 0.6563706563706564, 0.6563706563706564, 0.646830530401035, 0.6563706563706564, 0.6563706563706564]], [[0.6730083234244947, 0.672209026128266, 0.672189349112426, 0.672209026128266, 0.672189349112426, 0.672189349112426, 0.6714116251482799, 0.676923076923077, 0.67458432304038, 0.6737841043890866], [0.6542056074766354, 0.6542056074766354, 0.6542056074766354, 0.6542056074766354, 0.6559571619812583, 0.6550802139037434, 0.6550802139037434, 0.6542056074766354, 0.6542056074766354, 0.6542056074766354], [0.5809248554913294, 0.5816618911174786, 0.5800865800865801, 0.5809248554913294, 0.5800865800865801, 0.5816618911174786, 0.5800865800865801, 0.5800865800865801, 0.5824964131994261, 0.5809248554913294], [0.6511627906976745, 0.6520547945205478, 0.6511627906976745, 0.6538987688098495, 0.6501377410468319, 0.6538987688098495, 0.6538987688098495, 0.6511627906976745, 0.6520547945205478, 0.6520547945205478], [0.678709677419355, 0.678709677419355, 0.6804657179818887, 0.6803069053708439, 0.6795865633074936, 0.6778350515463918, 0.6785714285714285, 0.6803069053708439, 0.6785714285714285, 0.6794380587484036], [0.5816618911174786, 0.5680473372781065, 0.5684830633284241, 0.5680473372781065, 0.5659259259259258, 0.5680473372781065, 0.5667655786350148, 0.5667655786350148, 0.5672082717872968, 0.5680473372781065], [0.6270270270270271, 0.6336898395721926, 0.6261808367071525, 0.6345381526104418, 0.673992673992674, 0.6261808367071525, 0.6270270270270271, 0.6345381526104418, 0.6336898395721926, 0.6328437917222963], [0.5781021897810219, 0.695837780149413, 0.5781021897810219, 0.5781021897810219, 0.577259475218659, 0.5781021897810219, 0.5781021897810219, 0.576419213973799, 0.577259475218659, 0.5781021897810219], [0.5693215339233039, 0.563338301043219, 0.5693215339233039, 0.5625, 0.564179104477612, 0.5809248554913294, 0.5701624815361891, 0.5710059171597633, 0.5701624815361891, 0.5710059171597633]]]
results = np.array(raw_results)
results_mean = np.mean(results, 2)

df = pd.DataFrame(data=results_mean, columns=windows, index=sizes)
#df = df.pivot_table("Size of feature vectors", "Window", "val")

sns.set(style="white")
f, ax = plt.subplots(figsize=(8, 8))
cmap = sns.diverging_palette(220, 10, as_cmap=True)
sns.heatmap(df, cmap=cmap,  vmax=1.0, vmin=0.0,
               ax=ax, annot=True)

sns.plt.show()