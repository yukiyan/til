Threadは値を持たせられる。

```
$ irb
irb(main):001:0> Thread.current[:foo]
=> nil
irb(main):002:0> Thread.current[:foo] = 'hey'
=> "hey"
irb(main):003:0> Thread.current[:foo]
=> "hey"
irb(main):004:0> Thread.current.keys
=> [:foo]
```

```
irb(main):005:0> t=Thread.new{}
=> #<Thread:0x007fc8850cb278@(irb):5 run>
irb(main):006:0> t[:foo]
=> nil
irb(main):007:0> t[:foo] = 'foo'
=> "foo"
irb(main):008:0> t[:foo]
=> "foo"
```

[Class: Thread (Ruby 2.2.2)](http://ruby-doc.org/core-2.2.2/Thread.html#method-i-thread_variables)


新しく生成したスレッドについてはpush_tagsされておらず、こんな修正(一部改変)をする機会があったのでコードを読んだのがきっかけ。

```diff
threads << Thread.new do
+          Rails.logger.formatter.push_tags("hoge")
           fuga.run
         end
```

https://github.com/rails/rails/blob/v4.2.5.2/activesupport/lib/active_support/tagged_logging.rb#L45-L47
