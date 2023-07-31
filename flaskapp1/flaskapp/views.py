import random

from string import Template
from xml.dom import minidom

from . import app

#{{{1 minidom setup
def _elem_inplace_addition(self,other):
    self.appendChild(other)
    return self

def _elem_textnode(self,text):
    textnode = self.ownerDocument.createTextNode(text)
    self.appendChild(textnode)
    return self

def _elem_set_attributes_from_tuple(self,*args):
    for k,v in args:
        self.setAttribute(k,str(v))
    return self

minidom.Element.__iadd__ = _elem_inplace_addition
minidom.Element.txt = _elem_textnode
minidom.Element.attrt = _elem_set_attributes_from_tuple
minidom.Element.__str__ = lambda s:s.toprettyxml().strip()
#}}}1

#{{{1 Template
T = Template("""<!doctype html>
<html>
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <meta name="author" content="dustractor">
        <title>my fl studio html document background</title>
        <style>
            $style
        </style>
    </head>
    <body>
        $content
    </body>
</html>
""")

#}}}1

#{{{1 stylesheet
style = """
            body {
                background-color:#333333;
                font-family:sans-serif;
                font-size:16pt;
                padding:auto;
            }
            .container {
                vertical-align:center;
                padding:4rem;
                width:90%;
                height:90%;
                margin:auto;
                margin-top:8rem;
                display:flex;
                flex-direction:row;
                flex-wrap:wrap;
                justify-content:space-evenly;
                align-content:stretch;
                align-items:center;
                background-color:#303030;
                gap:1rem;
                border-radius:1rem;
            }
            .primetype {
                border-radius:1rem;
                background-color:#333;
                padding:1rem;
                margin:auto;
                color:#404040;
            }
            .primetype > h3 {
                position:relative;
                top:-3rem;
                left:-2rem;
            }
            .primetype > p {
                font-size:36pt;
            }


"""
#}}}1

#{{{1 prime lists

balanced_primes = [5,53,157,173,211,257,263,373,563,593,607,653,733,
 947,977,1103,1123,1187,1223,1367,1511,1747,1753,
 1907,2287,2417,2677,2903,2963,3307,3313,3637,3733,
 4013,4409,4457,4597,4657,4691,4993,5107,5113,5303,
 5387,5393]

chen_primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,47,53,59,67,
 71,83,89,101,107,109,113,127,131,137,139,149,157,
 167,179,181,191,197,199,211,227,233,239,251,257,
 263,269,281,293,307,311,317,337,347,353,359,379,
 389,401,409]

circular_primes = [2,3,5,7,11,13,17,31,37,71,73,79,97,113,131,197,
 199,311,337,373,719,733,919,971,991,1193,1931,
 3119,3779,7793,7937,9311,9377,11939,19391,19937,
 37199,39119,71993,91193,93719,93911,99371,193939,
 199933,319993]

cluster_primes = [3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,
 67,71,73,79,83,89,101,103,107,109,113,131,137,139,
 151,157,163,167,173,179,181,193,197,199,233,239,
 241,271,277,281,283,311,313,317,353,359,389,401,
 421,433]

eisenstein_primes = [2,5,11,17,23,29,41,47,53,59,71,83,89,101,107,113,
 131,137,149,167,173,179,191,197,227,233,239,251,
 257,263,269,281,293,311,317,347,353,359,383,389,
 401,419,431,443,449,461,467,479,491,503,509,521,
 557,563,569,587]

emirps = [13,17,31,37,71,73,79,97,107,113,149,157,167,179,
 199,311,337,347,359,389,701,709,733,739,743,751,
 761,769,907,937,941,953,967,971,983,991,1009,1021,
 1031,1033,1061,1069,1091,1097,1103,1109,1151,1153,
 1181,1193,1201]

euler_irregular_primes = [19,31,43,47,61,67,71,79,101,137,139,149,193,223,
 241,251,263,277,307,311,349,353,359,373,379,419,
 433,461,463,491,509,541,563,571,577,587,619,677,
 691,709,739,751,761,769,773,811,821,877,887,907,
 929,941,967,971,983]

fermat_primes = [3,5,17,257,65537]

fortunate_primes = [3,5,7,13,17,19,23,37,47,59,61,67,71,79,89,101,
 103,107,109,127,151,157,163,167,191,197,199,223,
 229,233,239,271,277,283,293,307,311,313,331,353,
 373,379,383,397,401,409,419,421,439,443,457,461,
 491,499,509]

gaussian_primes = [3,7,11,19,23,31,43,47,59,67,71,79,83,103,107,127,
 131,139,151,163,167,179,191,199,211,223,227,239,
 251,263,271,283,307,311,331,347,359,367,379,383,
 419,431,439,443,463,467,479,487,491,499,503,523,
 547,563,571]

good_primes = [5,11,17,29,37,41,53,59,67,71,97,101,127,149,179,
 191,223,227,251,257,269,307,311,331,347,419,431,
 541,557,563,569,587,593,599,641,727,733,739,809,
 821,853,929,937,967,1009,1031,1087,1151,1213,1277]

happy_primes = [7,13,19,23,31,79,97,103,109,139,167,193,239,263,
 293,313,331,367,379,383,397,409,487,563,617,653,
 673,683,709,739,761,863,881,907,937,1009,1033,
 1039,1093,1151,1277,1303,1373,1427,1447,1481,1487,
 1511,1607,1663]

harmonic_primes = [5,13,17,23,41,67,73,79,107,113,139,149,157,179,
 191,193,223,239,241,251,263,277,281,293,307,311,
 317,331,337,349,431,443,449,461,467,479,487,491,
 499,503,541,547,557,563,569,593,619,653,683,691,
 709,757,769,787]

higgs_primes = [2,3,5,7,11,13,19,23,29,31,37,43,47,53,59,61,67,
 71,79,101,107,127,131,139,149,151,157,173,181,191,
 197,199,211,223,229,263,269,277,283,311,317,331,
 347,349,367,373,383,397,419,421,431,461,463,491,
 509,523,547,557,571]

irregular_primes = [37,59,67,101,103,131,149,157,233,257,263,271,283,
 293,307,311,347,353,379,389,401,409,421,433,461,
 463,467,491,523,541,547,557,577,587,593,607,613,
 617,619,631,647,653,659,673,677,683,691,727,751,
 757,761,773,797,809,811,821,827,839,877,881,887,
 929,953,971,1061]

isolated_primes = [2,23,37,47,53,67,79,83,89,97,113,127,131,157,163,
 167,173,211,223,233,251,257,263,277,293,307,317,
 331,337,353,359,367,373,379,383,389,397,401,409,
 439,443,449,457,467,479,487,491,499,503,509,541,
 547,557,563]

lucky_primes = [3,7,13,31,37,43,67,73,79,127,151,163,193,211,223,
 241,283,307,331,349,367,409,421,433,463,487,541,
 577,601,613,619,631,643,673,727,739,769,787,823,
 883,937,991,997,1009,1021,1039,1087,1093,1117,
 1123]

minimal_primes = [2,3,5,7,11,19,41,61,89,409,449,499,881,991,6469,
 6949,9001,9049,9649,9949,60649,666649,946669,
 60000049,66000049,66600049]

palindromic_primes = [2,3,5,7,11,101,131,151,181,191,313,353,373,383,
 727,757,787,797,919,929,10301,10501,10601,11311,
 11411,12421,12721,12821,13331,13831,13931,14341,
 14741,15451,15551,16061,16361,16561,16661,17471,
 17971,18181] 

permutable_primes = [2,3,5,7,11,13,17,31,37,71,73,79,97,113,131,199,
 311,337,373,733,919,991,1111111111111111111,
 11111111111111111111111]

pierpont_primes = [2,3,5,7,13,17,19,37,73,97,109,163,193,257,433,
 487,577,769,1153,1297,1459,2593,2917,3457,3889,
 10369,12289,17497,18433,39367,52489,65537,139969,
 147457,209953,331777,472393,629857,746497,786433,
 839809,995329,1179649,1492993,1769473,1990657]

pillai_primes = [23,29,59,61,67,71,79,83,109,137,139,149,193,227,
 233,239,251,257,269,271,277,293,307,311,317,359,
 379,383,389,397,401,419,431,449,461,463,467,479,
 499,503,521,557,563,569,571,577,593,599,601,607]

primeval_primes = [2,13,37,107,113,137,1013,1237,1367,10079,10139,
 12379,13679,100279,100379,123479,1001237,1002347,
 1003679,1012379]

proth_primes = [3,5,13,17,41,97,113,193,241,257,353,449,577,641,
 673,769,929,1153,1217,1409,1601,2113,2689,2753,
 3137,3329,3457,4481,4993,6529,7297,7681,7937,9473,
 9601,9857,10369,10753,11393,11777,12161,12289,
 13313]

pythagorean_primes = [5,13,17,29,37,41,53,61,73,89,97,101,109,113,137,
 149,157,173,181,193,197,229,233,241,257,269,277,
 281,293,313,317,337,349,353,373,389,397,401,409,
 421,433,449,457,461,509,521,541,557,569,577,593,
 601,613,617]

prime_quadruplets_a = [5,11,101,191,821,1481,1871,2081,3251,3461,5651,
 9431,13001,15641,15731,16061,18041,18911,19421,
 21011,22271,25301,31721,34841,43781,51341,55331,
 62981,67211,69491,72221,77261,79691,81041,82721,
 88811,97841]

prime_quadruplets_b = [7,13,103,193,823,1483,1873,2083,3253,3463,5653,
 9433,13003,15643,15733,16063,18043,18913,19423,
 21013,22273,25303,31723,34843,43783,51343,55333,
 62983,67213,69493,72223,77263,79693,81043,82723,
 88813,97843]

prime_quadruplets_c = [11,17,107,197,827,1487,1877,2087,3257,3467,5657,
 9437,13007,15647,15737,16067,18047,18917,19427,
 21017,22277,25307,31727,34847,43787,51347,55337,
 62987,67217,69497,72227,77267,79697,81047,82727,
 88817,97847]

prime_quadruplets_d = [13,19,109,199,829,1489,1879,2089,3259,3469,5659,
 9439,13009,15649,15739,16069,18049,18919,19429,
 21019,22279,25309,31729,34849,43789,51349,55339,
 62989,67219,69499,72229,77269,79699,81049,82729,
 88819,97849]

ramanujan_primes = [2,11,17,29,41,47,59,67,71,97,101,107,127,149,151,
 167,179,181,227,229,233,239,241,263,269,281,307,
 311,347,349,367,373,401,409,419,431,433,439,461,
 487,491,503,569,571,587,593,599,601,607,641,643,
 647,653,659]

regular_primes = [3,5,7,11,13,17,19,23,29,31,41,43,47,53,61,71,73,
 79,83,89,97,107,109,113,127,137,139,151,163,167,
 173,179,181,191,193,197,199,211,223,227,229,239,
 241,251,269,277,281,313,317,331,337,349,359,367,
 373,383,397,419,431]

safe_primes = [5,7,11,23,47,59,83,107,167,179,227,263,347,359,
 383,467,479,503,563,587,719,839,863,887,983,1019,
 1187,1283,1307,1319,1367,1439,1487,1523,1619,1823,
 1907,2027,2039,2063,2099,2207,2447,2459,2579,2819,
 2879,2903,2963]

self_primes = [3,5,7,31,53,97,211,233,277,367,389,457,479,547,
 569,613,659,727,839,883,929,1021,1087,1109,1223,
 1289,1447,1559,1627,1693,1783,1873,2099,2213,2347,
 2437,2459,2503,2549,2593,2617,2683,2729,2819,2953,
 3023,3067]

solinas_primes = [3,5,7,11,13]

sophie_germain_primes = [2,3,5,11,23,29,41,53,83,89,113,131,173,179,191,
 233,239,251,281,293,359,419,431,443,491,509,593,
 641,653,659,683,719,743,761,809,911,953,1013,1019,
 1031,1049,1103,1223,1229,1289,1409,1439,1451,1481,
 1499,1511,1559]

super_primes = [3,5,11,17,31,41,59,67,83,109,127,157,179,191,211,
 241,277,283,331,353,367,401,431,461,509,547,563,
 587,599,617,709,739,773,797,859,877,919,967,991,
 1031,1063,1087,1153,1171,1201,1217,1297,1409,1433,
 1447,1471]

supersingular_primes = [2,3,5,7,11,13,17,19,23,29,31,41,47,59,71]

left_truncatable_primes = [2,3,5,7,13,17,23,37,43,47,53,67,73,83,97,113,137,
 167,173,197,223,283,313,317,337,347,353,367,373,
 383,397,443,467,523,547,613,617,643,647,653,673,
 683,743,773,797,823,853,883,937,947,953,967,983,
 997,1223]

right_truncatable_primes = [2,3,5,7,23,29,31,37,53,59,71,73,79,233,239,293,
 311,313,317,373,379,593,599,719,733,739,797,2333,
 2339,2393,2399,2939,3119,3137,3733,3739,3793,3797,
 5939,7193,7331,7333,7393,23333,23339,23399,23993,
 29399,31193]

two_sided_primes = [2,3,5,7,23,37,53,73,313,317,373,797,3137,3797,739397]

unique_primes = [3,11,37,101,9091,9901,333667,909091,99990001,
 999999000001,9999999900000001,909090909090909091,
 1111111111111111111,11111111111111111111111,
 900900900900990990990991,
 909090909090909090909090909091]
#}}}1

#{{{1 pick funcs

def pick_balanced_primes(n=1):
    if n == 1:
        return random.choices(balanced_primes,k=n)[0]
    else:
        return random.choices(balanced_primes,k=n)

def pick_chen_primes(n=1):
    if n == 1:
        return random.choices(chen_primes,k=n)[0]
    else:
        return random.choices(chen_primes,k=n)

def pick_circular_primes(n=1):
    if n == 1:
        return random.choices(circular_primes,k=n)[0]
    else:
        return random.choices(circular_primes,k=n)

def pick_cluster_primes(n=1):
    if n == 1:
        return random.choices(cluster_primes,k=n)[0]
    else:
        return random.choices(cluster_primes,k=n)

def pick_eisenstein_primes(n=1):
    if n == 1:
        return random.choices(eisenstein_primes,k=n)[0]
    else:
        return random.choices(eisenstein_primes,k=n)

def pick_emirps(n=1):
    if n == 1:
        return random.choices(emirps,k=n)[0]
    else:
        return random.choices(emirps,k=n)

def pick_euler_irregular_primes(n=1):
    if n == 1:
        return random.choices(euler_irregular_primes,k=n)[0]
    else:
        return random.choices(euler_irregular_primes,k=n)

def pick_fermat_primes(n=1):
    if n == 1:
        return random.choices(fermat_primes,k=n)[0]
    else:
        return random.choices(fermat_primes,k=n)

def pick_fortunate_primes(n=1):
    if n == 1:
        return random.choices(fortunate_primes,k=n)[0]
    else:
        return random.choices(fortunate_primes,k=n)

def pick_gaussian_primes(n=1):
    if n == 1:
        return random.choices(gaussian_primes,k=n)[0]
    else:
        return random.choices(gaussian_primes,k=n)

def pick_good_primes(n=1):
    if n == 1:
        return random.choices(good_primes,k=n)[0]
    else:
        return random.choices(good_primes,k=n)

def pick_happy_primes(n=1):
    if n == 1:
        return random.choices(happy_primes,k=n)[0]
    else:
        return random.choices(happy_primes,k=n)

def pick_harmonic_primes(n=1):
    if n == 1:
        return random.choices(harmonic_primes,k=n)[0]
    else:
        return random.choices(harmonic_primes,k=n)

def pick_higgs_primes(n=1):
    if n == 1:
        return random.choices(higgs_primes,k=n)[0]
    else:
        return random.choices(higgs_primes,k=n)

def pick_irregular_primes(n=1):
    if n == 1:
        return random.choices(irregular_primes,k=n)[0]
    else:
        return random.choices(irregular_primes,k=n)

def pick_isolated_primes(n=1):
    if n == 1:
        return random.choices(isolated_primes,k=n)[0]
    else:
        return random.choices(isolated_primes,k=n)

def pick_lucky_primes(n=1):
    if n == 1:
        return random.choices(lucky_primes,k=n)[0]
    else:
        return random.choices(lucky_primes,k=n)

def pick_minimal_primes(n=1):
    if n == 1:
        return random.choices(minimal_primes,k=n)[0]
    else:
        return random.choices(minimal_primes,k=n)

def pick_palindromic_primes(n=1):
    if n == 1:
        return random.choices(palindromic_primes,k=n)[0]
    else:
        return random.choices(palindromic_primes,k=n)

def pick_permutable_primes(n=1):
    if n == 1:
        return random.choices(permutable_primes,k=n)[0]
    else:
        return random.choices(permutable_primes,k=n)

def pick_pierpont_primes(n=1):
    if n == 1:
        return random.choices(pierpont_primes,k=n)[0]
    else:
        return random.choices(pierpont_primes,k=n)

def pick_pillai_primes(n=1):
    if n == 1:
        return random.choices(pillai_primes,k=n)[0]
    else:
        return random.choices(pillai_primes,k=n)

def pick_primeval_primes(n=1):
    if n == 1:
        return random.choices(primeval_primes,k=n)[0]
    else:
        return random.choices(primeval_primes,k=n)

def pick_proth_primes(n=1):
    if n == 1:
        return random.choices(proth_primes,k=n)[0]
    else:
        return random.choices(proth_primes,k=n)

def pick_pythagorean_primes(n=1):
    if n == 1:
        return random.choices(pythagorean_primes,k=n)[0]
    else:
        return random.choices(pythagorean_primes,k=n)

def pick_prime_quads():
    n = random.randint(0,36)
    return [prime_quadruplets_a[n],
            prime_quadruplets_b[n],
            prime_quadruplets_c[n],
            prime_quadruplets_d[n]]

def pick_ramanujan_primes(n=1):
    if n == 1:
        return random.choices(ramanujan_primes,k=n)[0]
    else:
        return random.choices(ramanujan_primes,k=n)

def pick_regular_primes(n=1):
    if n == 1:
        return random.choices(regular_primes,k=n)[0]
    else:
        return random.choices(regular_primes,k=n)

def pick_safe_primes(n=1):
    if n == 1:
        return random.choices(safe_primes,k=n)[0]
    else:
        return random.choices(safe_primes,k=n)

def pick_self_primes(n=1):
    if n == 1:
        return random.choices(self_primes,k=n)[0]
    else:
        return random.choices(self_primes,k=n)

def pick_solinas_primes(n=1):
    if n == 1:
        return random.choices(solinas_primes,k=n)[0]
    else:
        return random.choices(solinas_primes,k=n)

def pick_sophie_germain_primes(n=1):
    if n == 1:
        return random.choices(sophie_germain_primes,k=n)[0]
    else:
        return random.choices(sophie_germain_primes,k=n)

def pick_super_primes(n=1):
    if n == 1:
        return random.choices(super_primes,k=n)[0]
    else:
        return random.choices(super_primes,k=n)

def pick_supersingular_primes(n=1):
    if n == 1:
        return random.choices(supersingular_primes,k=n)[0]
    else:
        return random.choices(supersingular_primes,k=n)

def pick_left_truncatable_primes(n=1):
    if n == 1:
        return random.choices(left_truncatable_primes,k=n)[0]
    else:
        return random.choices(left_truncatable_primes,k=n)

def pick_right_truncatable_primes(n=1):
    if n == 1:
        return random.choices(right_truncatable_primes,k=n)[0]
    else:
        return random.choices(right_truncatable_primes,k=n)

def pick_two_sided_primes(n=1):
    if n == 1:
        return random.choices(two_sided_primes,k=n)[0]
    else:
        return random.choices(two_sided_primes,k=n)

def pick_unique_primes (n=1):
    if n == 1:
        return random.choices(unique_primes,k=n)[0]
    else:
        return random.choices(unique_primes,k=n)

#}}}1

#{{{1 indexroute
@app.route("/")
def indexroute(methods=["GET"]):

    doc = minidom.Document()
    elem = doc.createElement

    root = elem("div")
    root.attrt(("class","container"))

    # balanced_primes
    div = elem("div")
    div.attrt(("class","primetype"))
    h = elem("h3")
    h.txt("balanced")
    div += h
    p = elem("p")
    p.txt(repr(pick_balanced_primes()))
    div += p
    root += div

    # chen_primes
    div = elem("div")
    div.attrt(("class","primetype"))
    h = elem("h3")
    h.txt("chen")
    div += h
    p = elem("p")
    p.txt(repr(pick_chen_primes()))
    div += p
    root += div

    # circular_primes
    div = elem("div")
    div.attrt(("class","primetype"))
    h = elem("h3")
    h.txt("circular")
    div += h
    p = elem("p")
    p.txt(repr(pick_circular_primes()))
    div += p
    root += div

    # cluster_primes
    div = elem("div")
    div.attrt(("class","primetype"))
    h = elem("h3")
    h.txt("cluster")
    div += h
    p = elem("p")
    p.txt(repr(pick_cluster_primes()))
    div += p
    root += div

    # eisenstein_primes
    div = elem("div")
    div.attrt(("class","primetype"))
    h = elem("h3")
    h.txt("eisenstein")
    div += h
    p = elem("p")
    p.txt(repr(pick_eisenstein_primes()))
    div += p
    root += div

    # emirps
    div = elem("div")
    div.attrt(("class","primetype"))
    h = elem("h3")
    h.txt("emirps")
    div += h
    p = elem("p")
    p.txt(repr(pick_emirps()))
    div += p
    root += div

    # euler_irregular_primes
    div = elem("div")
    div.attrt(("class","primetype"))
    h = elem("h3")
    h.txt("euler irregular")
    div += h
    p = elem("p")
    p.txt(repr(pick_euler_irregular_primes()))
    div += p
    root += div

    # fermat_primes
    div = elem("div")
    div.attrt(("class","primetype"))
    h = elem("h3")
    h.txt("fermat")
    div += h
    p = elem("p")
    p.txt(repr(pick_fermat_primes()))
    div += p
    root += div

    # fortunate_primes
    div = elem("div")
    div.attrt(("class","primetype"))
    h = elem("h3")
    h.txt("fortunate")
    div += h
    p = elem("p")
    p.txt(repr(pick_fortunate_primes()))
    div += p
    root += div

    # gaussian_primes
    div = elem("div")
    div.attrt(("class","primetype"))
    h = elem("h3")
    h.txt("gaussian")
    div += h
    p = elem("p")
    p.txt(repr(pick_gaussian_primes()))
    div += p
    root += div

    # good_primes
    div = elem("div")
    div.attrt(("class","primetype"))
    h = elem("h3")
    h.txt("good")
    div += h
    p = elem("p")
    p.txt(repr(pick_good_primes()))
    div += p
    root += div

    # happy_primes
    div = elem("div")
    div.attrt(("class","primetype"))
    h = elem("h3")
    h.txt("happy")
    div += h
    p = elem("p")
    p.txt(repr(pick_happy_primes()))
    div += p
    root += div

    # harmonic_primes
    div = elem("div")
    div.attrt(("class","primetype"))
    h = elem("h3")
    h.txt("harmonic")
    div += h
    p = elem("p")
    p.txt(repr(pick_harmonic_primes()))
    div += p
    root += div

    # higgs_primes
    div = elem("div")
    div.attrt(("class","primetype"))
    h = elem("h3")
    h.txt("higgs")
    div += h
    p = elem("p")
    p.txt(repr(pick_higgs_primes()))
    div += p
    root += div

    # irregular_primes
    div = elem("div")
    div.attrt(("class","primetype"))
    h = elem("h3")
    h.txt("irregular")
    div += h
    p = elem("p")
    p.txt(repr(pick_irregular_primes()))
    div += p
    root += div

    # isolated_primes
    div = elem("div")
    div.attrt(("class","primetype"))
    h = elem("h3")
    h.txt("isolated")
    div += h
    p = elem("p")
    p.txt(repr(pick_irregular_primes()))
    div += p
    root += div

    # lucky_primes
    div = elem("div")
    div.attrt(("class","primetype"))
    h = elem("h3")
    h.txt("lucky")
    div += h
    p = elem("p")
    p.txt(repr(pick_lucky_primes()))
    div += p
    root += div

    # minimal_primes
    div = elem("div")
    div.attrt(("class","primetype"))
    h = elem("h3")
    h.txt("minimal")
    div += h
    p = elem("p")
    p.txt(repr(pick_minimal_primes()))
    div += p
    root += div

    # palindromic_primes
    div = elem("div")
    div.attrt(("class","primetype"))
    h = elem("h3")
    h.txt("palindromic")
    div += h
    p = elem("p")
    p.txt(repr(pick_palindromic_primes()))
    div += p
    root += div

    # permutable_primes
    div = elem("div")
    div.attrt(("class","primetype"))
    h = elem("h3")
    h.txt("permutable")
    div += h
    p = elem("p")
    p.txt(repr(pick_permutable_primes()))
    div += p
    root += div

    # pierpont_primes
    div = elem("div")
    div.attrt(("class","primetype"))
    h = elem("h3")
    h.txt("pierpont")
    div += h
    p = elem("p")
    p.txt(repr(pick_pierpont_primes()))
    div += p
    root += div

    # pillai_primes
    div = elem("div")
    div.attrt(("class","primetype"))
    h = elem("h3")
    h.txt("pillai")
    div += h
    p = elem("p")
    p.txt(repr(pick_pillai_primes()))
    div += p
    root += div

    # primeval_primes
    div = elem("div")
    div.attrt(("class","primetype"))
    h = elem("h3")
    h.txt("primeval")
    div += h
    p = elem("p")
    p.txt(repr(pick_primeval_primes()))
    div += p
    root += div

    # proth_primes
    div = elem("div")
    div.attrt(("class","primetype"))
    h = elem("h3")
    h.txt("proth")
    div += h
    p = elem("p")
    p.txt(repr(pick_proth_primes()))
    div += p
    root += div

    # pythagorean_primes
    div = elem("div")
    div.attrt(("class","primetype"))
    h = elem("h3")
    h.txt("pythagorean")
    div += h
    p = elem("p")
    p.txt(repr(pick_pythagorean_primes()))
    div += p
    root += div

    # prime_quadruplets
    div = elem("div")
    div.attrt(("class","primetype"))
    h = elem("h3")
    h.txt("quadruplet")
    div += h
    for n in pick_prime_quads():
        p = elem("p")
        p.txt(repr(n))
        div += p
    root += div


    # ramanujan_primes
    div = elem("div")
    div.attrt(("class","primetype"))
    h = elem("h3")
    h.txt("ramanujan")
    div += h
    p = elem("p")
    p.txt(repr(pick_ramanujan_primes()))
    div += p
    root += div

    # regular_primes
    div = elem("div")
    div.attrt(("class","primetype"))
    h = elem("h3")
    h.txt("regular")
    div += h
    p = elem("p")
    p.txt(repr(pick_regular_primes()))
    div += p
    root += div

    # safe_primes
    div = elem("div")
    div.attrt(("class","primetype"))
    h = elem("h3")
    h.txt("safe")
    div += h
    p = elem("p")
    p.txt(repr(pick_safe_primes()))
    div += p
    root += div

    # self_primes
    div = elem("div")
    div.attrt(("class","primetype"))
    h = elem("h3")
    h.txt("self")
    div += h
    p = elem("p")
    p.txt(repr(pick_self_primes()))
    div += p
    root += div

    # solinas_primes
    div = elem("div")
    div.attrt(("class","primetype"))
    h = elem("h3")
    h.txt("solinas")
    div += h
    p = elem("p")
    p.txt(repr(pick_solinas_primes()))
    div += p
    root += div

    # sophie_germain_primes
    div = elem("div")
    div.attrt(("class","primetype"))
    h = elem("h3")
    h.txt("sophie germain")
    div += h
    p = elem("p")
    p.txt(repr(pick_sophie_germain_primes()))
    div += p
    root += div

    # super_primes
    div = elem("div")
    div.attrt(("class","primetype"))
    h = elem("h3")
    h.txt("super")
    div += h
    p = elem("p")
    p.txt(repr(pick_super_primes()))
    div += p
    root += div

    # supersingular_primes
    div = elem("div")
    div.attrt(("class","primetype"))
    h = elem("h3")
    h.txt("supersingular")
    div += h
    p = elem("p")
    p.txt(repr(pick_supersingular_primes()))
    div += p
    root += div

    # left_truncatable_primes
    div = elem("div")
    div.attrt(("class","primetype"))
    h = elem("h3")
    h.txt("left-truncatable")
    div += h
    p = elem("p")
    p.txt(repr(pick_left_truncatable_primes()))
    div += p
    root += div

    # right_truncatable_primes
    div = elem("div")
    div.attrt(("class","primetype"))
    h = elem("h3")
    h.txt("right-truncatable")
    div += h
    p = elem("p")
    p.txt(repr(pick_right_truncatable_primes()))
    div += p
    root += div

    # two_sided_primes
    div = elem("div")
    div.attrt(("class","primetype"))
    h = elem("h3")
    h.txt("two-sided")
    div += h
    p = elem("p")
    p.txt(repr(pick_two_sided_primes()))
    div += p
    root += div

    # unique_primes 
    div = elem("div")
    div.attrt(("class","primetype"))
    h = elem("h3")
    h.txt("unique")
    div += h
    p = elem("p")
    p.txt(repr(pick_unique_primes()))
    div += p
    root += div


    content = str(root)

    return T.substitute(content=content,style=style)
    
#}}}1

