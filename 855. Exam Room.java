/*
In an exam room, there are N seats in a single row, numbered 0, 1, 2, ..., N-1.

When a student enters the room, they must sit in the seat that maximizes the distance to the closest person.  If there are multiple such seats, they sit in the seat with the lowest number.  (Also, if no one is in the room, then the student sits at seat number 0.)

Return a class ExamRoom(int N) that exposes two functions: ExamRoom.seat() returning an int representing what seat the student sat in, and ExamRoom.leave(int p) representing that the student in seat number p now leaves the room.  It is guaranteed that any calls to ExamRoom.leave(p) have a student sitting in seat p.



Example 1:

Input: ["ExamRoom","seat","seat","seat","seat","leave","seat"], [[10],[],[],[],[],[4],[]]
Output: [null,0,9,4,2,null,5]
Explanation:
ExamRoom(10) -> null
seat() -> 0, no one is in the room, then the student sits at seat number 0.
seat() -> 9, the student sits at the last seat number 9.
seat() -> 4, the student sits at the last seat number 4.
seat() -> 2, the student sits at the last seat number 2.
leave(4) -> null
seat() -> 5, the student sits at the last seat number 5.
​​​​​​​

Note:

1 <= N <= 10^9
ExamRoom.seat() and ExamRoom.leave() will be called at most 10^4 times across all test cases.
Calls to ExamRoom.leave(p) are guaranteed to have a student currently sitting in seat number p.
 */

// Accepted Solution with ArrayList. Dynamic memory usage.
import java.util.ArrayList;
class ExamRoom {

    int seatCount = 0;
    int n;
    ArrayList<Integer> seats = new ArrayList<Integer>();

    public ExamRoom(int N) {
        n = N;
    }

    public int seat() {
        if (seatCount == 0){
            seatCount++;
            seats.add(0);
            return 0;
        }
        seatCount++;
        int res = 0, prev = -1, st=-1;
        for (int i : seats) {
            if (prev == -1) {
                res = i;
                st = 0;
            } else if (res < (i-prev)/2) {
                res = (i-prev)/2;
                st = prev+res;
            }
            prev = i;
        }
        if (res < n-prev-1) {
            res = n-prev-1;
            st = n-1;
        }
        int k=seats.size();
        for (int i=0; i<k ; ++i ){
            if (st < seats.get(i)) {
                seats.add(i,st);
                break;
            }
        }
        if (k == seats.size()) seats.add(st);
        // System.out.println(st+" : "+seats);
        return st;
    }

    public void leave(int p) {
        seats.remove(new Integer(p));
        seatCount--;
    }
}

/**
 * Your ExamRoom object will be instantiated and called as such:
 * ExamRoom obj = new ExamRoom(N);
 * int param_1 = obj.seat();
 * obj.leave(p);
 */


// Time limit exceeded in this solution using Arrays. Memory Usage O(N)

import java.util.Arrays;
class ExamRoom {

    int seatCount = 0;
    int[] seats;

    public ExamRoom(int N) {
        seats = new int[N];
    }

    public int seat() {
        if (seatCount == 0){
            seatCount++;
            seats[0] = 1;
            return 0;
        }
        seatCount++;
        int res = 0, i, prev = -1, st=-1;
        for (i = 0; i<seats.length; i++) {
            if (seats[i] == 1) {
                if (prev == -1) {
                    res = i;
                    st = 0;
                } else if (res < (i-prev)/2) {
                    res = (i-prev)/2;
                    st = prev+res;
                }
                prev = i;
            }
        }
        if (res < i-prev-1) {
            res = i-prev-1;
            st = i-1;
        }
        seats[st] = 1;
        return st;
    }

    public void leave(int p) {
        seats[p] = 0;
//        System.out.println(Arrays.toString(seats));
        seatCount--;
    }
}

/**
 * Your ExamRoom object will be instantiated and called as such:
 * ExamRoom obj = new ExamRoom(N);
 * int param_1 = obj.seat();
 * obj.leave(p);
 */
