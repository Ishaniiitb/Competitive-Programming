fun main() {
    val t = readLine()!!.toInt()
    repeat(t) {
        val (x, y) = readLine()!!.split(" ")
        var l = y.length - 1
        var k = 0
        var steps = 0
        var yInt = y.toInt()
        val xInt = x.toInt()
        while (l >= 0) {
            val n = yInt / (xInt * 10.0.pow(l).toInt())
            if (n == 0) {
                l--
                continue
            } else {
                yInt -= n * xInt * 10.0.pow(l).toInt()
                steps += n
            }
        }
        steps += yInt
        println(steps)
    }
}
