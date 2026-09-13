class ListNode {
    int val;
    ListNode next;

    public ListNode(int val){
        this(val, null);
    }

    public ListNode(int val, ListNode next){
        this.val = val;
        this.next = next;
    }
}


class LinkedList {
    private ListNode head;
    private ListNode tail;

    public LinkedList() {
        this.head = new ListNode(-1);
        this.tail = this.head;
    }

    public int get(int index) {
        ListNode curr = head.next;
        int i = 0;
        while(curr != null){
            if(i == index){
                return curr.val;
            }
            i++;
            curr = curr.next;
        }
        return -1;
    }

    public void insertHead(int val) {
        ListNode newNode = new ListNode(val);
        newNode.next = head.next;
        head.next = newNode;
        if(newNode.next == null){
            tail = newNode;
        } 
    }

    public void insertTail(int val) {
        ListNode newTail = new ListNode(val);
        tail.next = newTail;
        tail = newTail;


    }

    public boolean remove(int index) {
        if (head.next == null){
            return false;
        }

        ListNode current = head;
        int currentNode = 0;
        while(currentNode != index ){
            if(current.next == null){ 
                return false;
            }
            current = current.next;
            currentNode++;

        }
        if(current.next == null){
            return false;
        }
        
        if(current.next == tail){
            tail = current;
        }
        current.next = current.next.next;

        return true;
        
    }

    public ArrayList<Integer> getValues() {
        ArrayList<Integer> values = new ArrayList<>();
        ListNode curr = head;
        while(curr.next != null){
            curr = curr.next;
            values.add(curr.val);
        }
        return values;

    }
}
