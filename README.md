# ctf
My code for various capture the flag competitions

## Things i would like to remember

### How to recognize AES while reversing

AES S-BOX starts with

```
 63h, 7Ch, 77h, 7Bh, 0F2h, 6Bh, 6Fh
```

if we see this, there is AES somewhere, usually this is used when the key is set.

Sometimes the use of AES looks something like this:
```
set_key(stuff)  <--- S BOX here   
set_iv(stuff)
AES_encrypt(stuff)
```

### Useful things sometimes

- Functions always have the same pre and post, can be used as known-plain-test attack.

- https://github.com/makomk/aeskeyfind <--- find AES keys in memory dumps

- "golang.org/x/net/bpf" is BPF filter decompiler (used in a challenge here: https://github.com/Kasimir123/CTFWriteUps/tree/main/03-2021-Zer0pts/Syscall-777)

- wasm2c -> gcc -c game.c -I wabt/wasm2c/ -I wabt/third_party/wasm-c-api/include/   (to compile wasm into c and try to open in IDA/ghidra)
