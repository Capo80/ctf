from pwn import *
sock_filter stru_B00[205] =
[
  [ 32, 0, 0, 0 ],  # ldabsw src, dst, imm
  [ 21, 0, 200, 777 ],
  [ 32, 0, 0, 16 ],
  [ 84, 0, 0, 255 ],
  [ 53, 199, 0, 128 ],
  [ 32, 0, 0, 16 ],
  [ 116, 0, 0, 8 ],
  [ 84, 0, 0, 255 ],
  [ 53, 195, 0, 128 ],
  [ 32, 0, 0, 16 ],
  [ 116, 0, 0, 16 ],
  [ 84, 0, 0, 255 ],
  [ 53, 191, 0, 128 ],
  [ 32, 0, 0, 16 ],
  [ 116, 0, 0, 24 ],
  [ 84, 0, 0, 255 ],
  [ 53, 187, 0, 128 ],
  [ 32, 0, 0, 16 ],
  [ 2, 0, 0, 0 ],
  [ 32, 0, 0, 24 ],
  [ 97, 0, 0, 0 ],
  [ 172, 0, 0, 0 ],
  [ 2, 0, 0, 1 ],
  [ 32, 0, 0, 32 ],
  [ 97, 0, 0, 1 ],
  [ 172, 0, 0, 0 ],
  [ 2, 0, 0, 2 ],
  [ 32, 0, 0, 40 ],
  [ 97, 0, 0, 2 ],
  [ 172, 0, 0, 0 ],
  [ 2, 0, 0, 3 ],
  [ 96, 0, 0, 0 ],
  [ 97, 0, 0, 1 ],
  [ 12, 0, 0, 0 ],
  [ 97, 0, 0, 2 ],
  [ 12, 0, 0, 0 ],
  [ 97, 0, 0, 3 ],
  [ 12, 0, 0, 0 ],
  [ 2, 0, 0, 4 ],
  [ 96, 0, 0, 0 ],
  [ 97, 0, 0, 1 ],
  [ 28, 0, 0, 0 ],
  [ 97, 0, 0, 2 ],
  [ 12, 0, 0, 0 ],
  [ 97, 0, 0, 3 ],
  [ 28, 0, 0, 0 ],
  [ 2, 0, 0, 5 ],
  [ 96, 0, 0, 0 ],
  [ 97, 0, 0, 1 ],
  [ 12, 0, 0, 0 ],
  [ 97, 0, 0, 2 ],
  [ 28, 0, 0, 0 ],
  [ 97, 0, 0, 3 ],
  [ 28, 0, 0, 0 ],
  [ 2, 0, 0, 6 ],
  [ 96, 0, 0, 0 ],
  [ 97, 0, 0, 1 ],
  [ 28, 0, 0, 0 ],
  [ 97, 0, 0, 2 ],
  [ 28, 0, 0, 0 ],
  [ 97, 0, 0, 3 ],
  [ 12, 0, 0, 0 ],
  [ 2, 0, 0, 7 ],
  [ 96, 0, 0, 4 ],
  [ 97, 0, 0, 5 ],
  [ 76, 0, 0, 0 ],
  [ 2, 0, 0, 8 ],
  [ 96, 0, 0, 6 ],
  [ 97, 0, 0, 7 ],
  [ 92, 0, 0, 0 ],
  [ 97, 0, 0, 8 ],
  [ 172, 0, 0, 0 ],
  [ 2, 0, 0, 8 ],
  [ 96, 0, 0, 5 ],
  [ 97, 0, 0, 6 ],
  [ 76, 0, 0, 0 ],
  [ 2, 0, 0, 9 ],
  [ 96, 0, 0, 7 ],
  [ 97, 0, 0, 4 ],
  [ 92, 0, 0, 0 ],
  [ 97, 0, 0, 9 ],
  [ 172, 0, 0, 0 ],
  [ 2, 0, 0, 9 ],
  [ 96, 0, 0, 6 ],
  [ 97, 0, 0, 7 ],
  [ 76, 0, 0, 0 ],
  [ 2, 0, 0, 10 ],
  [ 96, 0, 0, 4 ],
  [ 97, 0, 0, 5 ],
  [ 92, 0, 0, 0 ],
  [ 97, 0, 0, 10 ],
  [ 172, 0, 0, 0 ],
  [ 2, 0, 0, 10 ],
  [ 96, 0, 0, 7 ],
  [ 97, 0, 0, 4 ],
  [ 76, 0, 0, 0 ],
  [ 2, 0, 0, 11 ],
  [ 96, 0, 0, 5 ],
  [ 97, 0, 0, 6 ],
  [ 92, 0, 0, 0 ],
  [ 97, 0, 0, 11 ],
  [ 172, 0, 0, 0 ],
  [ 2, 0, 0, 11 ],
  [ 96, 0, 0, 8 ],
  [ 21, 37, 0, 4127179254 ],
  [ 21, 20, 0, 1933881070 ],
  [ 21, 31, 0, 4255576062 ],
  [ 21, 10, 0, 1670347938 ],
  [ 21, 15, 0, 2720551936 ],
  [ 21, 26, 0, 2307981054 ],
  [ 21, 29, 0, 2673307092 ],
  [ 21, 10, 0, 4139379682 ],
  [ 21, 15, 0, 4192373742 ],
  [ 21, 20, 0, 530288564 ],
  [ 21, 29, 0, 4025255646 ],
  [ 21, 14, 0, 3747612986 ],
  [ 21, 3, 0, 3098492862 ],
  [ 21, 14, 0, 2130820044 ],
  [ 96, 0, 0, 9 ],
  [ 21, 50, 84, 4056898606 ],
  [ 96, 0, 0, 9 ],
  [ 21, 32, 82, 3064954302 ],
  [ 96, 0, 0, 9 ],
  [ 21, 24, 80, 3602496994 ],
  [ 96, 0, 0, 9 ],
  [ 21, 34, 78, 1627051272 ],
  [ 96, 0, 0, 9 ],
  [ 21, 34, 76, 2002783966 ],
  [ 96, 0, 0, 9 ],
  [ 21, 28, 74, 4088827598 ],
  [ 96, 0, 0, 9 ],
  [ 21, 36, 72, 1340672294 ],
  [ 96, 0, 0, 9 ],
  [ 21, 12, 70, 2115580844 ],
  [ 96, 0, 0, 9 ],
  [ 21, 36, 68, 530288564 ],
  [ 96, 0, 0, 9 ],
  [ 21, 28, 66, 3415533530 ],
  [ 96, 0, 0, 9 ],
  [ 21, 10, 64, 3116543486 ],
  [ 96, 0, 0, 9 ],
  [ 21, 14, 62, 251771212 ],
  [ 96, 0, 0, 9 ],
  [ 21, 20, 60, 4126139894 ],
  [ 96, 0, 0, 9 ],
  [ 21, 6, 58, 2813168974 ],
  [ 96, 0, 0, 10 ],
  [ 21, 46, 56, 2130523044 ],
  [ 96, 0, 0, 10 ],
  [ 21, 36, 54, 3606265306 ],
  [ 96, 0, 0, 10 ],
  [ 21, 38, 52, 3151668710 ],
  [ 96, 0, 0, 10 ],
  [ 21, 34, 50, 614968622 ],
  [ 96, 0, 0, 10 ],
  [ 21, 42, 48, 3086875838 ],
  [ 96, 0, 0, 10 ],
  [ 21, 16, 46, 251771212 ],
  [ 96, 0, 0, 10 ],
  [ 21, 18, 44, 3015552726 ],
  [ 96, 0, 0, 10 ],
  [ 21, 34, 42, 1627379644 ],
  [ 96, 0, 0, 10 ],
  [ 21, 12, 40, 1601724370 ],
  [ 96, 0, 0, 10 ],
  [ 21, 18, 38, 665780030 ],
  [ 96, 0, 0, 10 ],
  [ 21, 14, 36, 3281895882 ],
  [ 96, 0, 0, 10 ],
  [ 21, 30, 34, 1301225350 ],
  [ 96, 0, 0, 10 ],
  [ 21, 20, 32, 2583645294 ],
  [ 96, 0, 0, 10 ],
  [ 21, 6, 30, 3917315412 ],
  [ 96, 0, 0, 11 ],
  [ 21, 27, 28, 2673307092 ],
  [ 96, 0, 0, 11 ],
  [ 21, 25, 26, 1532821474 ],
  [ 96, 0, 0, 11 ],
  [ 21, 23, 24, 3119098870 ],
  [ 96, 0, 0, 11 ],
  [ 21, 21, 22, 3917315412 ],
  [ 96, 0, 0, 11 ],
  [ 21, 19, 20, 2174343406 ],
  [ 96, 0, 0, 11 ],
  [ 21, 17, 18, 666819390 ],
  [ 96, 0, 0, 11 ],
  [ 21, 15, 16, 4143147994 ],
  [ 96, 0, 0, 11 ],
  [ 21, 13, 14, 1827055294 ],
  [ 96, 0, 0, 11 ],
  [ 21, 11, 12, 4290701286 ],
  [ 96, 0, 0, 11 ],
  [ 21, 9, 10, 197094626 ],
  [ 96, 0, 0, 11 ],
  [ 21, 7, 8, 2145762244 ],
  [ 96, 0, 0, 11 ],
  [ 21, 5, 6, 2720880308 ],
  [ 96, 0, 0, 11 ],
  [ 21, 3, 4, 3120414398 ],
  [ 96, 0, 0, 11 ],
  [ 21, 1, 2, 3708166042 ],
  [ 6, 0, 0, 2147418112 ],
  [ 6, 0, 0, 327680 ],
  [ 6, 0, 0, 327681 ]
];

#define BPF_MAJOR_VERSION 1
#define BPF_MINOR_VERSION 1

/*
 *	Try and keep these values and structures similar to BSD, especially
 *	the BPF code definitions which need to match so you can share filters
 */
 
struct sock_filter {	/* Filter block */
	__u16	code;   /* Actual filter code */
	__u8	jt;	/* Jump true */
	__u8	jf;	/* Jump false */
	__u32	k;      /* Generic multiuse field */
};

struct sock_fprog {	/* Required for SO_ATTACH_FILTER. */
	unsigned short		len;	/* Number of filter blocks */
	struct sock_filter __user *filter;
};

/*
 * Instruction classes
 */

#define BPF_CLASS(code) ((code) & 0x07)
#define         BPF_LD          0x00
#define         BPF_LDX         0x01
#define         BPF_ST          0x02
#define         BPF_STX         0x03
#define         BPF_ALU         0x04
#define         BPF_JMP         0x05
#define         BPF_RET         0x06
#define         BPF_MISC        0x07

/* ld/ldx fields */
#define BPF_SIZE(code)  ((code) & 0x18)
#define         BPF_W           0x00
#define         BPF_H           0x08
#define         BPF_B           0x10
#define BPF_MODE(code)  ((code) & 0xe0)
#define         BPF_IMM         0x00
#define         BPF_ABS         0x20
#define         BPF_IND         0x40
#define         BPF_MEM         0x60
#define         BPF_LEN         0x80
#define         BPF_MSH         0xa0

/* alu/jmp fields */
#define BPF_OP(code)    ((code) & 0xf0)
#define         BPF_ADD         0x00
#define         BPF_SUB         0x10
#define         BPF_MUL         0x20
#define         BPF_DIV         0x30
#define         BPF_OR          0x40
#define         BPF_AND         0x50
#define         BPF_LSH         0x60
#define         BPF_RSH         0x70
#define         BPF_NEG         0x80
#define		BPF_MOD		0x90
#define		BPF_XOR		0xa0

#define         BPF_JA          0x00
#define         BPF_JEQ         0x10
#define         BPF_JGT         0x20
#define         BPF_JGE         0x30
#define         BPF_JSET        0x40
#define BPF_SRC(code)   ((code) & 0x08)
#define         BPF_K           0x00
#define         BPF_X           0x08

/* ret - BPF_K and BPF_X also apply */
#define BPF_RVAL(code)  ((code) & 0x18)
#define         BPF_A           0x10

/* misc */
#define BPF_MISCOP(code) ((code) & 0xf8)
#define         BPF_TAX         0x00
#define         BPF_TXA         0x80

#ifndef BPF_MAXINSNS
#define BPF_MAXINSNS 4096
#endif

/*
 * Macros for filter block array initializers.
 */
#ifndef BPF_STMT
#define BPF_STMT(code, k) { (unsigned short)(code), 0, 0, k }
#endif
#ifndef BPF_JUMP
#define BPF_JUMP(code, k, jt, jf) { (unsigned short)(code), jt, jf, k }
#endif

/*
 * Number of scratch memory words for: BPF_ST and BPF_STX
 */
#define BPF_MEMWORDS 16

/* RATIONALE. Negative offsets are invalid in BPF.
   We use them to reference ancillary data.
   Unlike introduction new instructions, it does not break
   existing compilers/optimizers.
 */
#define SKF_AD_OFF    (-0x1000)
#define SKF_AD_PROTOCOL 0
#define SKF_AD_PKTTYPE 	4
#define SKF_AD_IFINDEX 	8
#define SKF_AD_NLATTR	12
#define SKF_AD_NLATTR_NEST	16
#define SKF_AD_MARK 	20
#define SKF_AD_QUEUE	24
#define SKF_AD_HATYPE	28
#define SKF_AD_RXHASH	32
#define SKF_AD_CPU	36
#define SKF_AD_ALU_XOR_X	40
#define SKF_AD_VLAN_TAG	44
#define SKF_AD_VLAN_TAG_PRESENT 48
#define SKF_AD_MAX	52
#define SKF_NET_OFF   (-0x100000)
#define SKF_LL_OFF    (-0x200000)



p = process("./chall")

p.sendline("mario")

print(p.recv())

