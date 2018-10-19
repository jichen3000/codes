from heapq import heappush, heappop
class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        height_q = []
        points = []
        # len(buildings).p()
        for i in range(len(buildings)-1, 0, -1):
            # pre one is larger than cur one, remove cur one
            if buildings[i-1][2] >= buildings[i][2] and buildings[i-1][0] <= buildings[i][0] and buildings[i-1][1] >= buildings[i][1]:
                del buildings[i]
            # same high, merge to pre one, remove cur one
            elif buildings[i][2] == buildings[i-1][2]:
                buildings[i-1][1] = buildings[i][1]
                del buildings[i]
        for l, r, h in buildings:
            heappush(points, (l,h,"left"))
            heappush(points, (r,h,"right"))

        pre_h = 0
        results = []
        while points:
            v, h, pos = heappop(points)
            # (v, h, pos, pre_h).p()
            if pos == "left":
                if h > pre_h:
                    if pre_h > 0: heappush(height_q,-pre_h)
                    pre_h = h
                    # same x value
                    if results and results[-1][0] == v:
                        results[-1][1] = pre_h
                    else:
                        results += [v, pre_h],
                else:
                    heappush(height_q,-h)
            else:
                if h == pre_h:
                    pre_h = -heappop(height_q) if len(height_q) > 0 else 0
                    results += [v, pre_h],
                else:
                    height_q.remove(-h)
                    heapify(height_q)
            # (pre_h, height_q, results).p()
        return results

    # my best solution nlogn, best one
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        height_q = []
        points = []
        # len(buildings).p()
        for i in range(len(buildings)-1, 0, -1):
            # pre one is larger than cur one, remove cur one
            if buildings[i-1][2] >= buildings[i][2] and buildings[i-1][0] <= buildings[i][0] \
                    and buildings[i-1][1] >= buildings[i][1]:
                del buildings[i]
            # same high, merge to pre one, remove cur one
            elif buildings[i][2] == buildings[i-1][2]:
                buildings[i-1][1] = buildings[i][1]
                del buildings[i]
        for l, r, h in buildings:
            heappush(points, (l,h,"left",r))
            heappush(points, (r,h,"right", 0))

        pre_h, pre_r = 0, -1
        results = []
        while points:
            v, h, pos, r = heappop(points)
            # (v, h, pos, r, pre_h, pre_r).p()
            if pos == "left":
                if h > pre_h:
                    if pre_h > 0: heappush(height_q,(-pre_h,pre_r))
                    pre_h, pre_r = h, r
                    # same x value
                    if results and results[-1][0] == v:
                        results[-1][1] = pre_h
                    else:
                        results += [v, pre_h],
                else:
                    heappush(height_q,(-h,r))
            else:
                if h == pre_h:
                    while height_q:
                        pre_h, pre_r = heappop(height_q)
                        if pre_r > v:
                            pre_h = -pre_h
                            break
                    else:
                        pre_h, pre_r = 0, -1
                    results += [v, pre_h],
        return results


    # https://briangordon.github.io/2014/08/the-skyline-problem.html
    # critical points loop, n**2
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        # add this part, it can pass all testcases, but speed is very slow
        for i in range(len(buildings)-1, 0, -1):
            # pre one is larger than cur one, remove cur one
            if buildings[i-1][2] >= buildings[i][2] and buildings[i-1][0] <= buildings[i][0] \
                    and buildings[i-1][1] >= buildings[i][1]:
                del buildings[i]
            # same high, merge to pre one, remove cur one
            elif buildings[i][2] == buildings[i-1][2]:
                buildings[i-1][1] = buildings[i][1]
                del buildings[i]

        point_heap = []
        for l, r, h in buildings:
            heappush(point_heap, [l, h])
            heappush(point_heap, [r, 0])
        points = []
        while point_heap:
            points += heappop(point_heap),
        for l, r, h in buildings:
            for p in points:
                if l <= p[0] and p[0] < r:
                    p[1] = max(p[1], h)
                elif p[0] >= r:
                    break
        for i in range(len(points)-2,-1, -1):
            if points[i+1][1] == points[i][1]:
                del points[i+1]
        return points


class Solution(object):
    # review
    # not fastest, but easy to understand
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        vh_list = []
        for l, r, h in buildings:
            vh_list += (l, h, "left"),
            vh_list += (r, h, "right"),
        # vh_list.sort(key=lambda x:(x[0],-x[1]))
        vh_list.sort()
        # vh_list.p()
        res = []
        pre_h_list = []
        max_h = 0
        for v, h, pos in vh_list:
            if pos == "left":
                if len(pre_h_list) == 0 or h > max_h:
                    if res and res[-1][0] == v:
                        res[-1][1] = h
                    else:
                        res += [v, h],
                    max_h = h
                pre_h_list += h,
            else:
                pre_h_list.remove(h)
                if h == max_h:
                    max_h = max(pre_h_list) if pre_h_list else 0
                    if max_h != h:
                        res += [v, max_h],
        return res

class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        from heapq import heappush, heappop
        acc, res = [], []
        while buildings or acc:
            # acc.p()
            # buildings.p()
            if len(acc) == 0 or (buildings and acc[0][1]>=buildings[0][0]):
                x, r, h = buildings.pop(0)
                # (x,r,h).p()
                # if buildings and acc: (acc[0][1]>buildings[0][0]).p()
                if acc and h < -acc[0][0]:
                    heappush(acc, (-h,r))
                    continue
                heappush(acc, (-h,r))
            else:
                h, x = heappop(acc)
                while acc and acc[0][1] < x:
                    heappop(acc)
            h = -acc[0][0] if acc else 0
            if res and x == res[-1][0]:
                res[-1][1] = h
            elif res and h == res[-1][1]:
                continue
            else:
                res += [x, h],
        return res

if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        # buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
        # Solution().getSkyline(buildings).must_equal(
        #         [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]])
        # buildings = [[0,2,3],[2,5,3]]
        # Solution().getSkyline(buildings).must_equal(
        #         [[0,3],[5,0]])
        # buildings = [[2,9,10],[9,12,15]]
        # Solution().getSkyline(buildings).must_equal(
        #         [[2,10],[9,15],[12,0]])
        # buildings = [[1,2,1],[1,2,2],[1,2,3]]
        # Solution().getSkyline(buildings).must_equal(
        #         [[1,3],[2,0]])

        buildings = [[0,2,3],[2,4,3],[4,6,3]]
        Solution().getSkyline(buildings).must_equal(
                [[0, 3], [6, 0]])
        buildings = [[3,7,8],[3,8,7],[3,9,6]]
        Solution().getSkyline(buildings).must_equal(
                [[3,8],[7,7],[8,6],[9,0]])
        buildings = [[1,3,1],[2,4,2],[3,5,1]]
        Solution().getSkyline(buildings).must_equal(
                [[1,1],[2,2],[4,1],[5,0]])

        buildings = [[2,4,70],[3,8,30],[6,100,41],[7,15,70],[10,30,102],[15,25,76],[60,80,91],[70,90,72],[85,120,59]]
        Solution().getSkyline(buildings).must_equal(
                [[2, 70], [4, 30], [6, 41], [7, 70], [10, 102], [30, 41], [60, 91], [80, 72], [90, 59], [120, 0]])

        buildings = [[2190,661048,758784],[9349,881233,563276],[12407,630134,38165],[22681,726659,565517],[31035,590482,658874],[41079,901797,183267],[41966,103105,797412],[55007,801603,612368],[58392,212820,555654],[72911,127030,629492],[73343,141788,686181],[83528,142436,240383],[84774,599155,787928],[106461,451255,856478],[108312,994654,727797],[126206,273044,692346],[134022,376405,472351],[151396,993568,856873],[171466,493683,664744],[173068,901140,333376],[179498,667787,518146],[182589,973265,394689],[201756,900649,31050],[215635,818704,576840],[223320,282070,850252],[252616,974496,951489],[255654,640881,682979],[287063,366075,76163],[291126,900088,410078],[296928,373424,41902],[297159,357827,174187],[306338,779164,565403],[317547,979039,172892],[323095,698297,566611],[323195,622777,514005],[333003,335175,868871],[334996,734946,720348],[344417,952196,903592],[348009,977242,277615],[351747,930487,256666],[363240,475567,699704],[365620,755687,901569],[369650,650840,983693],[370927,621325,640913],[371945,419564,330008],[415109,890558,606676],[427304,782478,822160],[439482,509273,627966],[443909,914404,117924],[446741,853899,285878],[480389,658623,986748],[545123,873277,431801],[552469,730722,574235],[556895,568292,527243],[568368,728429,197654],[593412,760850,165709],[598238,706529,500991],[604335,921904,990205],[627682,871424,393992],[630315,802375,714014],[657552,782736,175905],[701356,827700,70697],[712097,737087,157624],[716678,889964,161559],[724790,945554,283638],[761604,840538,536707],[776181,932102,773239],[855055,983324,880344]]
        Solution().getSkyline(buildings).must_equal([[2190,758784],[41966,797412],[103105,787928],[106461,856478],[151396,856873],[252616,951489],[369650,983693],[480389,986748],[604335,990205],[921904,951489],[974496,880344],[983324,856873],[993568,727797],[994654,0]])
        
        buildings = [[2302,521688,394023],[10396,840253,671644],[22633,740538,553794],[33104,968793,842909],[33566,749635,5965],[34724,567056,645908],[38397,976841,114857],[41596,756920,756376],[42323,568307,228042],[50775,387740,218538],[61200,430269,411341],[76753,128525,68496],[79373,804949,468753],[81162,945496,354439],[83491,488856,82703],[83809,615534,135829],[91172,98128,912707],[95567,530117,871928],[101588,239875,783665],[103078,590123,714837],[103699,628880,670340],[106349,601107,634192],[114080,857023,390674],[127529,156548,766654],[137072,782287,221710],[139108,668109,706758],[141344,450521,304555],[147516,954217,783723],[147543,822521,605998],[152329,865672,871749],[155260,725627,85938],[157561,672597,545652],[161181,795511,915546],[165951,657821,612662],[168914,648886,559332],[176974,403872,328905],[177537,816528,832605],[178894,994383,245167],[179305,756396,288023],[205335,698945,602609],[212822,529316,389301],[229320,301090,412311],[237431,802167,532853],[241799,432691,875928],[267123,868784,764314],[282273,563128,851718],[282813,337595,839969],[293252,872759,547091],[294475,588008,544742],[310848,575608,8816],[313543,702058,619704],[325577,888559,912371],[330608,552502,212597],[332655,726247,322151],[356504,578275,261647],[357551,420868,893362],[358688,445854,822451],[359730,411661,261651],[367095,705352,206884],[368783,930183,526370],[369792,438228,17430],[372046,918137,417386],[384795,779748,89023],[385884,954729,987280],[390022,543892,949489],[419733,989088,752157],[422927,835825,640265],[424969,556942,208378],[437284,468376,167867],[441169,712058,143721],[452677,730601,452847],[453781,899636,4472],[455288,861562,314782],[465055,497234,610455],[468848,953512,993894],[564747,800626,521581],[569498,632750,102677],[580055,865963,52393],[590629,767024,328585],[594183,729278,559762],[633995,710904,837755],[637204,972619,56114],[640775,884992,894921],[643236,732511,895800],[645857,777086,452259],[663772,852581,904928],[665117,673222,153191],[673219,810151,736462],[683913,859158,474705],[691729,895602,974107],[695824,730590,525683],[744533,979535,858112],[751142,866326,818831],[758572,830775,838557],[789925,989097,188384],[823175,949879,924869],[871352,970590,706320],[874124,958946,58789],[879565,947487,883632],[883183,910077,337730],[888036,936787,995802]]
        Solution().getSkyline(buildings).must_equal([[2302,394023],[10396,671644],[33104,842909],[91172,912707],[98128,871928],[161181,915546],[385884,987280],[468848,993894],[888036,995802],[936787,993894],[953512,987280],[954729,858112],[979535,752157],[989088,245167],[994383,0]])
        
        buildings = [[1, 3, 4],[2, 6, 1],[4, 16, 2],[5, 8, 4],[7, 10, 8],[8, 9, 6],[11, 13, 7],[12, 15, 5],[14, 17, 3]]
        Solution().getSkyline(buildings).must_equal(
                [[1, 4], [3, 1], [4, 2], [5, 4], [7, 8], [10, 2], [11, 7], [13, 5], [15, 3], [17, 0]])



